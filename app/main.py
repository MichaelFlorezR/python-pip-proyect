import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('world_population.csv')
  """
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
"""
  country = input('Type Country => ').title()
  name = country

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(name, labels, values)


#el siguiente condicional indica que este modulo solo se ejecutará si se ejecuta desde el mismo.
#si se importa desde otro modulo, tendra que llamarse la funcion que se desee ejecutar
if __name__ == "__main__":
    run()