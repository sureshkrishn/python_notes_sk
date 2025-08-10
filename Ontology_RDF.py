#Resource Description Framework
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Create a new RDF graph
g = Graph()

# Load your ontology file
ontology_file = "common_sense_ontology.ttl"
g.parse(ontology_file, format="turtle")

# Define namespaces
ns = dict(
    ex=g.namespace_manager.absolutize("ex:", None),
    rdf=g.namespace_manager.absolutize("rdf:", None),
    rdfs=g.namespace_manager.absolutize("rdfs:", None)
)

# Query your ontology
# For example, let's find all fruits and their colors
query = """
    SELECT ?fruit ?color
    WHERE {
        ?fruit rdf:type ex:Fruit .
        ?fruit ex:hasColor ?color .
    }
"""

results = g.query(query, initNs=ns)

print("Fruits and their colors:")
for row in results:
    print(f"{row[0].n3(ns)} has color {row[1].n3(ns)}")

# Add new statements to your ontology
# For example, let's add that "Orange" is a type of "Fruit" and has the color "Orange"
new_fruit = ns['ex'] + URIRef("Orange")
g.add((new_fruit, RDF.type, ns['ex'] + URIRef("Fruit")))
g.add((new_fruit, ns['ex'] + URIRef("hasColor"), Literal("Orange")))

# Serialize and print the modified ontology
print("\nModified ontology:")
print(g.serialize(format="turtle"))