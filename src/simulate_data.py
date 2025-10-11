import numpy as np
import pandas as pd
from pathlib import Path
import random
from score import compute_severity

# Constants
N_SUBJECTS = 60
SYMPTOMS = [
    "ardor", "picor", "sensacion_cuerpo_extraño", "lagrimeo", "parpadeo_excesivo",
    "enrojecimiento_ocular", "dolor_ocular", "pesadez_parpados", "sequedad",
    "vision_borrosa", "vision_doble", "dificultad_al_enfocar",
    "aumento_sensiblidad_luz", "halos_de_colores", "sensacion_de_ver_peor",
    "dolor_de_cabeza"
]

def generate_demographic_data(n_subjects=N_SUBJECTS):
    """Generate demographic and work-related variables following specified distributions."""
    df = pd.DataFrame()
    
    # Continuous variables
    df['edad'] = np.random.normal(34, 6, n_subjects).round().astype(int)
    df['edad'] = df['edad'].clip(25, 50)  # reasonable age range
    
    df['experiencia_radiologia'] = np.random.normal(4.3, 3.2, n_subjects).round(1)
    df['experiencia_radiologia'] = df['experiencia_radiologia'].clip(1, 15)
    
    # Generate tiempo_de_exposicion with positive correlation to future SVI scores
    df['tiempo_de_exposicion'] = np.random.normal(12, 4, n_subjects).round()
    df['tiempo_de_exposicion'] = df['tiempo_de_exposicion'].clip(8, 16)
    
    df['duracion_de_jornada'] = np.random.normal(12, 4, n_subjects).round()
    df['duracion_de_jornada'] = df['duracion_de_jornada'].clip(6, 16)
    
    # Categorical variables
    df['sexo'] = np.random.choice([0, 1], n_subjects, p=[0.5, 0.5])
    df['estado_civil'] = np.random.choice([0, 1, 2, 3], n_subjects, p=[0.4, 0.4, 0.1, 0.1])
    df['ingresos_mensuales'] = np.random.choice([0, 1, 2, 3], n_subjects, p=[0.1, 0.3, 0.5, 0.1])
    df['condiciones_oculares'] = np.random.choice([0, 1], n_subjects, p=[0.4, 0.6])
    df['lentes'] = np.random.choice([0, 1], n_subjects, p=[0.4, 0.6])
    df['iluminacion'] = np.random.choice([0, 1], n_subjects, p=[0.2, 0.8])
    df['frecuencia_de_pausas'] = np.random.choice([0, 1, 2], n_subjects, p=[0.2, 0.5, 0.3])
    df['uso_de_dispositivos'] = np.random.choice([0, 1, 2, 3], n_subjects, p=[0.05, 0.15, 0.1, 0.7])
    df['distancia_hacia_el_monitor'] = np.random.choice([0, 1, 2], n_subjects, p=[0.2, 0.6, 0.2])
    
    return df

def generate_symptom_responses(tiempo_exposicion, target_svi_prop=0.7):
    """Generate CVS-Q responses ensuring target SVI proportion and correlation with tiempo_exposicion."""
    
    # Base probability for symptoms increases with tiempo_exposicion
    base_prob = (tiempo_exposicion - 8) / 8  # Normalize to 0-1 range
    base_prob = np.clip(base_prob, 0.2, 0.8)  # Ensure reasonable range
    
    freqs = []
    ints = []
    
    # Generate responses for each symptom
    for _ in SYMPTOMS:
        # Probability of having the symptom increases with tiempo_exposicion
        symptom_prob = np.random.normal(base_prob, 0.2)
        symptom_prob = np.clip(symptom_prob, 0, 1)
        
        # Generate frequency (0=never, 1=occasionally, 2=often)
        if np.random.random() > symptom_prob:
            freq = 0
            intensity = 0
        else:
            freq = np.random.choice([1, 2], p=[0.6, 0.4])
            intensity = np.random.choice([1, 2], p=[0.7, 0.3])
            
        freqs.append(freq)
        ints.append(intensity)
    
    # Calculate total severity
    severities = [compute_severity(f, i) for f, i in zip(freqs, ints)]
    total_severity = sum(severities)
    
    return freqs, ints, severities, total_severity

def generate_dataset(n_subjects=N_SUBJECTS, target_svi_prop=0.7):
    """Generate complete dataset with demographic data and CVS-Q responses."""
    # Generate base demographic data
    df = generate_demographic_data(n_subjects)
    
    # Add symptom columns
    for symptom in SYMPTOMS:
        df[f"{symptom}_frecuencia"] = 0
        df[f"{symptom}_intensidad"] = 0
        df[f"{symptom}_severidad"] = 0
    
    # Generate responses ensuring target SVI proportion
    total_severities = []
    
    for idx, row in df.iterrows():
        freqs, ints, sevs, total = generate_symptom_responses(row['tiempo_de_exposicion'])
        
        # Assign to DataFrame
        for symptom, freq, intensity, severity in zip(SYMPTOMS, freqs, ints, sevs):
            df.at[idx, f"{symptom}_frecuencia"] = freq
            df.at[idx, f"{symptom}_intensidad"] = intensity
            df.at[idx, f"{symptom}_severidad"] = severity
        
        total_severities.append(total)
    
    df['puntaje_sindrome_visual_informatico'] = total_severities
    df['svi'] = (df['puntaje_sindrome_visual_informatico'] >= 6).astype(int)
    
    # Adjust responses if needed to meet target SVI proportion
    current_svi_prop = df['svi'].mean()
    
    if current_svi_prop < target_svi_prop:
        # Increase some scores to meet target
        non_svi_mask = df['svi'] == 0
        n_to_convert = int((target_svi_prop - current_svi_prop) * n_subjects)
        convert_idx = df[non_svi_mask].sample(n=n_to_convert).index
        
        for idx in convert_idx:
            # Regenerate responses until SVI threshold is met
            while df.loc[idx, 'puntaje_sindrome_visual_informatico'] < 6:
                freqs, ints, sevs, total = generate_symptom_responses(
                    df.loc[idx, 'tiempo_de_exposicion'],
                    target_svi_prop=0.8  # Increase probability
                )
                if total >= 6:
                    for symptom, freq, intensity, severity in zip(SYMPTOMS, freqs, ints, sevs):
                        df.at[idx, f"{symptom}_frecuencia"] = freq
                        df.at[idx, f"{symptom}_intensidad"] = intensity
                        df.at[idx, f"{symptom}_severidad"] = severity
                    df.at[idx, 'puntaje_sindrome_visual_informatico'] = total
                    df.at[idx, 'svi'] = 1
                    break
    
    # Add severity categories
    df['severidad_svi'] = pd.cut(
        df['puntaje_sindrome_visual_informatico'],
        bins=[-float('inf'), 5, 10, 20, float('inf')],
        labels=['No SVI', 'Leve', 'Moderado', 'Severo']
    )
    
    return df

def main():
    """Generate and save synthetic dataset."""
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Generate dataset
    df = generate_dataset()
    
    # Save to CSV
    output_dir = Path("data/2_processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "df_models_synthetic.csv"
    df.to_csv(output_path, index=False)
    
    # Print summary statistics
    print("\nDataset Summary:")
    print(f"Total subjects: {len(df)}")
    print(f"SVI prevalence: {df['svi'].mean():.1%}")
    print("\nSeverity distribution:")
    print(df['severidad_svi'].value_counts(normalize=True))
    
    # Correlation between tiempo_de_exposicion and total score
    corr = df['tiempo_de_exposicion'].corr(df['puntaje_sindrome_visual_informatico'])
    print(f"\nCorrelation (tiempo_exposicion vs score): {corr:.3f}")

if __name__ == "__main__":
    main()