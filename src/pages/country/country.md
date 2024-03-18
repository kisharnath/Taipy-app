# **Country**{: .color-primary} Statistics

<|layout|column=1|
<|{default_country}|selector|lov={default_country}|on_change=on_change_country|dropdown|label=Country|>

|>

<|card|
Total earhtquake <|{len(data_by_specific_country)}|> 
|>
<br/>
<|{data_by_specific_country}|chart|type=histogram|x=Area|y=magnitude|height=600px|>


