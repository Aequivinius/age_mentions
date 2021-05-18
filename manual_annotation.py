def extract_columns(inpath, outpath):
    import pandas

    dataf = pandas.read_csv(inpath, sep='\t')
    dataf[['portal_url', 'text_raw']].to_csv(outpath, sep='\t', index=False)


def gate_to_tsv(inpath, outpath):
    from lxml import etree as ET

    with open(inpath, 'r', encoding='utf-8') as xml_file:
        tree = ET.parse(xml_file)

        root = tree.getroot()
        outstrings = []
        for annotation in root.findall(".//Annotation"):
            outstring = ''
            position = ','.join([annotation.get('StartNode'),
                                 annotation.get('EndNode')])

            about = ''
            confidence = ''
            for feature in annotation.findall(".//Feature"):
                if feature.find('Name').text == 'about':
                    if feature.find('Value').text:
                        about = feature.find('Value').text

                if feature.find('Name').text == 'confidence':
                    confidence = feature.find('Value').text
            outstring = '\t'.join([position, confidence, about])
            outstrings.append(outstring)

        annostring = '\t'.join(outstrings)

        textnode = root.find('.//TextWithNodes')
        ET.strip_tags(textnode, 'Node')
        # rawtext = textnode.text

    with open(outpath, 'w') as f:
        # f.write(rawtext + '\t' + annostring)
        f.write(annostring)
