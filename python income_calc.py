# Freelance Income Calculator - CLI (Spain Autonomo)
hours_week = float(input("Hours/week (e.g. 20): "))
rate = float(input("Rate €/h (e.g. 20): "))
hours_month = hours_week * 4
gross = hours_month * rate
irpf = gross * 0.21  # IRPF tax
ss = 300  # Autonomo quota
net = gross - irpf - ss
print(f"\n=== RESULTS ===")
print(f"Gross monthly: €{gross:.2f}")
print(f"IRPF (21%): -€{irpf:.2f}")
print(f"SS quota: -€{ss:.2f}")
print(f"NET TAKE-HOME: €{net:.2f}")
