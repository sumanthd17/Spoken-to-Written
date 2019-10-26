The Repo contains code for spoken english to written english converter

## Features Implemented:

### 1. Spoken to currency to numbers

```
Input:  convert three thousand six hundred to number
Output:  convert 3600 to number

Input:  convert two thousand three hundred dollars to number
Output:  convert $2300 to number

Input:  convert two pounds to number
Output:  convert £2 to number
```

### 2. Covert words to short forms

```
Input:  convert triple A to shortform
Output:  convert AAA to shortform
```

### 3. Combine abbreviation short forms

```
Input:  where is the P M O office
Output:  where is the PMO office
```

### Installation
```
python setup.py install
pip install -r requirements.txt
```

### Usage
```
from spoken2written import S2W

input_text = 'convert triple A to number. Where is the P M O office. convert two dollars to number'

s2w = S2W(input_text)

output_text = s2w.driver()
```

### Final Input and Output
```
Input:  convert triple A to number. Where is the P M O office. convert two dollars to number
Output:  convert AAA to number. where is the PMO offic. convert $2 to number
```

### Use Individual features
```
output_text = s2w.findAbbreviation(input_text)
output_text = s2w.word2num(input_text)
output_text = s2w.combineAbbreviations(input_text)
```