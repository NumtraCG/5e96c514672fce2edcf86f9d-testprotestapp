import json
import Connectors
import Transformations
import AutoML
try:
    testprotestapp_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e96c514672fce2edcf86f9e", spark, "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    testprotestapp_AutoFE = Transformations.TransformationMain.run(["5e96c514672fce2edcf86f9e"], {
                                                                   "5e96c514672fce2edcf86f9e": testprotestapp_DBFS}, "5e96c514672fce2edcf86f9f", spark, json.dumps({"FE": []}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(testprotestapp_AutoFE, [], "")

except Exception as ex:
    print(ex)
