import subprocess

#inserire path completo!
query_path = "/Users/liadraetta/Desktop/community-research-ontology/queries/work_query.sparql"
output_path = "/Users/liadraetta/Desktop/community-research-ontology/output/nt_output/pubblications.ttl"
jar_path = "../sparql-anything.jar"  # Update with the correct JAR file name

command = [
    "java", "-jar", jar_path,
    "-q", query_path,
    "-o", output_path,
    "-f", "nt"
]

result = subprocess.run(command, capture_output=True, text=True)
if result.returncode == 0:
    print(f"SPARQL Anything executed successfully. Output saved to {output_path}")
else:
    print(f"Error: {result.stderr}")