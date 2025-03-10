import subprocess

#inserire path completo!
query_path = "/Users/liadraetta/Desktop/community-research-ontology/queries/work_query.sparql"
output_path = "/Users/liadraetta/Desktop/community-research-ontology/output/nt_output/pubblications.ttl"
jar_path = "../sparql-anything.jar"

command = [
    "java", "-jar", jar_path,
    "-q", query_path,
    "-o", output_path,
    "-f", "nt"
]

result = subprocess.run(command, capture_output=True, text=True)