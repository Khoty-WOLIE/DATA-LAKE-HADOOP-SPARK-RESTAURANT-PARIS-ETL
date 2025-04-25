import xml.etree.ElementTree as ET
import csv
import os

input_folder = os.path.expanduser("~/code/data/paris")
output_file = "restaurants_paris.csv"

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "lat", "lon", "name"])

    for filename in os.listdir(input_folder):
        if filename.endswith(".osm"):
            path = os.path.join(input_folder, filename)
            tree = ET.parse(path)
            root = tree.getroot()

            for node in root.findall("node"):
                tags = {tag.attrib["k"]: tag.attrib["v"] for tag in node.findall("tag")}
                if tags.get("amenity") == "restaurant":
                    writer.writerow([
                        node.attrib.get("id"),
                        node.attrib.get("lat"),
                        node.attrib.get("lon"),
                        tags.get("name", "N/A")
                    ])

