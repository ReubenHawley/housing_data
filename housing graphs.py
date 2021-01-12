import pandas as pd

df = pd.read_csv('Bestaande_woningen__ontwikkeling_aanbod.csv')
df = df.drop(columns=[
    'Te koop staande woningen/Gem. aanbodtijd per vraagprijsklasse/350.000 tot 500.000 euro (maanden)',
    'Te koop staande woningen/Gem. aanbodtijd per vraagprijsklasse/500.000 tot 5.000.000 euro (maanden)',
    'Te koop staande woningen/Gebruiksoppervlakte/250 tot 500 m² (aantal)',
    'Te koop staande woningen/Vraagprijsklasse/350.000 tot 500.000 euro (aantal)',
    'Te koop staande woningen/Vraagprijsklasse/500.000 tot 5.000.000 euro (aantal)'
    ])
df.to_csv('Bestaande_woningen__ontwikkeling_aanbod_parsed.csv')
df2 = df.loc[(df['Woningtype','Perioden','Te koop staande woningen/Vraagprijsklasse/Totaal (aantal)','Te koop staande woningen/Vraagprijsklasse/50.000 tot 150.000 euro (aantal)','Te koop staande woningen/Vraagprijsklasse/150.000 tot 200.000 euro (aantal)','Te koop staande woningen/Vraagprijsklasse/200.000 tot 250.000 euro (aantal)','Te koop staande woningen/Vraagprijsklasse/250.000 tot 350.000 euro (aantal)'])]
print(df.head())
