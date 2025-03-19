import subprocess

# Script che restituisce output in formato .nt
#inserire path completo!
query_path = "/Users/liadraetta/Desktop/community-research-ontology/queries/author_query.sparql"
print(query_path)
output_path = "/output/nt_data/person.ttl"
jar_path = "../sparql-anything.jar"

command = [
    "java", "-jar", jar_path,
    "-q", query_path,
    "-o", output_path,
    "-f", "nt"
]

result = subprocess.run(command, capture_output=True, text=True)

