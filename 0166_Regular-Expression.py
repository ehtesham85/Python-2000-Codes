# Regular Expression

import re

pattern="South Africa"
# pattern=r"[A-Z]frica"
text='''
South Africa was under one of the world’s strictest Covid lockdowns which included a ban on alcohol and cigarette sales. And the economic impact of the pandemic for the socio-economically marginalised masses was devastating. Their distress was borne out by social researchers and impact analysts who predicted that the extreme poverty rate among vulnerable households had tripled. The social assistance measures announced by the government still left about 45% of South African workers without relief and the Labour Quarterly surveys found that close to three million people – around 18% of total employment – were working in the informal/parallel sector.
South Africa government has provided some relief. The authorities allocated ZAR 30bn ($1.6 bn) to a special National Disaster Benefit Fund and set up a Solidarity Fund to pool funds from government, businesses, and private individuals. The government is currently implementing a Covid–19 pandemic stimulus package of ZAR 500bn ($26.3 bn) equivalent to 10% of GDP, distributed as a loan guarantee scheme (40%); job protection and worker income (28%), tax relief (14%); social grants (1%); COVID–19 health-related services (4%), and municipality emergency services (4%). On 5 May 2020, the National Treasury Strategy 2020–2025 presented plans for the first time to mobilise $10bn from multilateral development banks to support the economy.South Africa is a good country.
'''
# match = re.search(pattern, text)
# print(match)

# matches = re.finditer(pattern, text)
# for match in matches:
#   print(match)

matches = re.finditer(pattern, text)
for match in matches:
  print(match.span())
  print(text[match.span()[0]:match.span()[1]])
  
  
