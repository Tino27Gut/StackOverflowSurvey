# 🧑‍💻 StackOverflowSurvey
###### Data Analytics Project in Qlik Sense Analyzing StackOverflow Survey Data

<br />

## 🔎 What You'll Find
This repository contains the ETL process, Qlik Script and Qlik App for the StackOverflow annual survey data spanning from 2021 to 2023. The data has been analyzed using QlikSense, resulting in an application that presents various analyses:
1. DB Engines and Languages Analysis
2. Salary Analysis
3. Developer Roles Analysis
4. Data Roles Preferences

## 🏗️ Project Structure
The project follows a Best Practices Framework and is organized into the following folders:
- 📁 00_Configuration: global configuration storing main variables, routes, and functions.
- 📁 01_Data: contains source files used for data extraction.
- 📁 02_Qvd: stores data in Qlik Sense proprietary file types. Includes 'Extraction (Ext)' and 'Transformation (Tra)' folders for raw and transformed data respectively.
- 📁 03_Qvs: holds Qlik Sense scripts for data extraction and transformation, organized into 'Extraction (Ext)' and 'Transformation (Tra)' sub-divisions.
- 📁 04_Py: contains Python scripts for more complex transformations not feasible in Qlik Sense.

## 🤔 Key Differences from StackOverflow's Analysis
While StackOverflow provides its own [survey analysis](https://survey.stackoverflow.com/2023/), this project differs in several ways:
- **Currency Conversion:** utilizes average monthly rates from a trusted source ([BIS](https://data.bis.org/)) for consistent compensation data across years.
- **Salary Data Adjustments:** addresses inconsistencies in SO's salary data, standardizing values and filtering outliers for clarity.
- **Years Considered:** includes data from 2021 to 2023 for comparative analysis, unlike SO which focuses on 2022 and 2023.
- **Fields Considered:** considers only fields available across all surveyed years for consistent analysis.

## ⚠️ Considerations
- **Questionnaire Changes:** note changes in answer types over survey years, affecting comparability.
- **Scope of Analysis:** while robust, some fields may not have been utilized; future iterations could deepen the analysis.
- **Currency Mapping:** some currencies are not mapped in BIS; alternative sources may be considered in future updates.

## 🔗 Sources
- [Stack Overflow Annual Developer Survey](https://survey.stackoverflow.co/)
- [BIS Bilateral Exchange Rates](https://data.bis.org/topics/XRU/data?rows=REF_AREA%7CCURRENCY&cols=TIME_PERIOD&settings=asc%7Cdesc%7Cname&data_view=table&filter=CURRENCY%3DAFN%257CDZD%257CAOA%257CARS%257CAWG%257CAUD%257CAZN%257CBSD%257CBHD%257CTHB%257CPAB%257CBBD%257CBYN%257CBZD%257CVEF%257CBOB%257CBAM%257CBRL%257CBND%257CBIF%257CCVE%257CCAD%257CKYD%257CXAF-XOF%257CCLP%257CCOP%257CKMF%257CCDF%257CNIO%257CCRC%257CCZK%257CGMD%257CDKK%257CMKD%257CDJF%257CDOP%257CVND%257CAMD%257CXCD%257CEGP%257CSVC%257CETB%257CEUR%257CFJD%257CHUF%257CGHS%257CHTG%257CPYG%257CGTQ%257CGNF%257CGYD%257CHKD%257CUAH%257CISK%257CINR%257CIRR%257CIQD%257CJMD%257CJOD%257CKES%257CPGK%257CKWD%257CMMK%257CLAK%257CGEL%257CLBP%257CALL%257CHNL%257CSLL%257CBGN%257CLRD%257CLYD%257CSZL%257CLSL%257CMGA%257CMWK%257CMYR%257CMRO%257CMUR%257CMXN%257CMDL%257CMAD%257CMZN%257CNGN%257CERN%257CNAD%257CNPR%257CANG%257CILS%257CTWD%257CNZD%257CBTN%257CNOK%257COMR%257CTOP%257CPKR%257CMOP%257CPHP%257CGBP%257CBWP%257CQAR%257CCNY%257CKHR%257CRON%257CMVR%257CIDR%257CRUB%257CRWF%257CSTD%257CSAR%257CRSD%257CSCR%257CSGD%257CPEN%257CSBD%257CKGS%257CZAR%257CSSP%257CXDR%257CLKR%257CSDG%257CUZS%257CSRD%257CSEK%257CCHF%257CSYP%257CTJS%257CBDT%257CWST%257CTZS%257CKZT%257CTTD%257CMNT%257CTND%257CTRY%257CTMT%257CAED%257CUGX%257CUYU%257CUSD%257CVUV%257CKRW%257CYER%257CJPY%257CZMW%257CZWL%257CPLN%255EYEAR%3D2023%257C2022%257C2021%255EFREQ%3DM%255EREF_AREA_TXT%3DAlgeria%257CAngola%257CBenin%257CBotswana%257CBurkina%2520Faso%257CBurundi%257CCabo%2520Verde%257CCameroon%257CCentral%2520African%2520Republic%257CChad%257CComoros%257CC%25C3%25B4te%2520d%27Ivoire%257CDemocratic%2520Republic%2520of%2520the%2520Congo%257CDjibouti%257CEgypt%257CEquatorial%2520Guinea%257CEritrea%257CEswatini%257CEthiopia%257CGabon%257CGhana%257CGuinea%257CGuinea-Bissau%257CKenya%257CLesotho%257CLiberia%257CLibya%257CMadagascar%257CMalawi%257CMali%257CMauritania%257CMauritius%257CMorocco%257CMozambique%257CNamibia%257CNiger%257CNigeria%257CRepublic%2520of%2520Congo%257CRwanda%257CSenegal%257CSeychelles%257CSierra%2520Leone%257CSouth%2520Africa%257CSouth%2520Sudan%257CSudan%257CS%25C3%25A3o%2520Tom%25C3%25A9%2520and%2520Pr%25C3%25ADncipe%257CTanzania%257CThe%2520Gambia%257CTogo%257CTunisia%257CUganda%257CZambia%257CZimbabwe%257CAfrica%257CAnguilla%257CAntigua%2520and%2520Barbuda%257CArgentina%257CAruba%257CBarbados%257CBelize%257CBolivia%257CBrazil%257CCanada%257CCayman%2520Islands%257CChile%257CColombia%257CCosta%2520Rica%257CDominica%257CDominican%2520Republic%257CEl%2520Salvador%257CGrenada%257CGuatemala%257CGuyana%257CHaiti%257CHonduras%257CJamaica%257CMexico%257CMontserrat%257CNicaragua%257CPanama%257CParaguay%257CPeru%257CSt%2520Kitts%2520and%2520Nevis%257CSt%2520Lucia%257CSt%2520Vincent%2520and%2520the%2520Grenadines%257CSuriname%257CThe%2520Bahamas%257CTrinidad%2520and%2520Tobago%257CUnited%2520States%257CUruguay%257CVenezuela%257CAmericas%257CAfghanistan%257CArmenia%257CAzerbaijan%257CBahrain%257CBangladesh%257CBhutan%257CBrunei%257CCambodia%257CChina%257CChinese%2520Taipei%257CCyprus%257CGeorgia%257CHong%2520Kong%2520SAR%257CIndia%257CIndonesia%257CIran%257CIraq%257CIsrael%257CJapan%257CJordan%257CKazakhstan%257CKorea%257CKuwait%257CKyrgyz%2520Republic%257CLaos%257CLebanon%257CMacao%2520SAR%257CMalaysia%257CMaldives%257CMongolia%257CMyanmar%257CNepal%257COman%257CPakistan%257CPhilippines%257CQatar%257CSaudi%2520Arabia%257CSingapore%257CSri%2520Lanka%257CSyria%257CTajikistan%257CThailand%257CTurkmenistan%257CT%25C3%25BCrkiye%257CUnited%2520Arab%2520Emirates%257CUzbekistan%257CVietnam%257CYemen%257CAsia%257CAlbania%257CAustria%257CBelarus%257CBelgium%257CBosnia%2520and%2520Herzegovina%257CBulgaria%257CCroatia%257CCzechia%257CDenmark%257CEstonia%257CFinland%257CFrance%257CGermany%257CGreece%257CHungary%257CIceland%257CIreland%257CItaly%257CLatvia%257CLithuania%257CLuxembourg%257CMalta%257CMoldova%257CMontenegro%257CNetherlands%257CNorth%2520Macedonia%257CNorway%257CPoland%257CPortugal%257CRomania%257CRussia%257CSan%2520Marino%257CSerbia%257CSlovakia%257CSlovenia%257CSpain%257CSweden%257CSwitzerland%257CUkraine%257CUnited%2520Kingdom%257CEurope%257CAustralia%257CFiji%257CKiribati%257CMicronesia%257CNew%2520Zealand%257CPapua%2520New%2520Guinea%257CSamoa%257CSolomon%2520Islands%257CTonga%257CVanuatu%257COceania%257CEuro%2520area%257CNetherlands%2520Antilles%257CWaemu%257CWorld%257CBIS%27%2520aggregates%2520%2F%2520Other%255ECOLLECTION%3DE)

<br />

This project offers a comprehensive view of developer's and data role's landscapes, based on StackOverflow survey data. Feel free to explore, contribute, or extend the analysis as needed.

##
