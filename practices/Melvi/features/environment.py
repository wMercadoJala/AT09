def before_all(context):
    print ("test")
    context.test="esto es una prueba"
def before_scenario(context, scenario):
    print("*****Before scenario*********")
    print(scenario.name)
    if "regresion" in scenario.tags:
        print("*****",scenario.tags,"*********")
    context.test = "+++++++++Hi scenarioAT-09+++++++"
