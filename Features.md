## Futere Features

### 1. Spell corrections

```
The spellings in the text could be wrongly detected by the speech to text model or the data in general might contian some spelling mistakes.
These can be corrected using edit distance or k-gram overlap available in stanford NLP
```

### 2. Combine words and numbers to convert into written format

```
Example: 
Input:  convert double o seven to shortform
Output:  convert oo seven to shortform
```

### 3. Covert Time into the corresponding format

```
Example:
Input:	convert seven thirty A M to time format
Output:	convert 7:30 AM to time format
```

### 4. Punctuation and Grammer

```
We may miss punctuations while speaking but while reading it is important to include punctions
```

### Design

```
My Implementation for the spoken to written is Object Oriented. The main class can be imported as a package and each feature is a function in the class.
So all the new features can be added a function in the class definition and correspondingly used as S2W.function_name()
I'm parsing the whole paragraph by breaking it into sentences and applying all features. So each feature doesn't interfere with other features and they all exist independently.
```