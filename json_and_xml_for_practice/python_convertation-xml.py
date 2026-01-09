import xml.etree.ElementTree as ET

xml_data = """
<person>
    <name>Nikita</name>
    <age>22</age>
    <position>qa_middle</position>
    <address>
        <street>maslovka</street>
        <house_number>211</house_number>
        <get_info>
            <house_id>21</house_id>
            <garage>3</garage>
            <elevator>4</elevator>
            <people>42</people>
        </get_info>
        <company>sber</company>
        <project>SPL</project>
        <info>
            <developers>
                <back_end>6</back_end>
                <front_end>2</front_end>
            </developers>
            <pm>
                <count>1</count>
            </pm>
            <po>
                <count>2</count>
            </po>
        </info>
    </address>
</person>
"""

xml_root = ET.fromstring(xml_data)
print(xml_root.find("address/info/po/count").text)