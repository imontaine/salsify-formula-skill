# Salsify Formula Function Reference

Source: Salsify “Formulas Cheat Sheet”
Source last modified: June 3, 2026
Extracted: July 30, 2026

## Summary

- 128 documented formula-language entries
- 127 callable functions
- 1 language construct: `LET...IN`

Names, syntax, descriptions, example formulas, and outputs below were extracted from the Salsify source page. Property IDs and sample values are Salsify’s examples.

## Quick index

- [`ADD`](#add)
- [`AINDEX`](#aindex)
- [`AND`](#and)
- [`ARRAY_SUM`](#array-sum)
- [`ASSET`](#asset)
- [`ASSET_VALUE`](#asset-value)
- [`ASSET_VALUES`](#asset-values)
- [`AT`](#at)
- [`CHANNEL_STATUS_FROM`](#channel-status-from)
- [`CLEAN_TEXT`](#clean-text)
- [`COALESCE`](#coalesce)
- [`COLLECTION`](#collection)
- [`COMPACT`](#compact)
- [`COMPOUND`](#compound)
- [`CONCAT_ARRAY`](#concat-array)
- [`CONCATENATE`](#concatenate)
- [`CONTAINS`](#contains)
- [`CREATED_AT`](#created-at)
- [`CURRENT_LOCALE`](#current-locale)
- [`CURRENT_PROPERTY_ID`](#current-property-id)
- [`CURRENT_PROPERTY_INDEX`](#current-property-index)
- [`DATA_INHERITANCE_HIERARCHY_LEVEL`](#data-inheritance-hierarchy-level)
- [`DATE_LAST_PUBLISHED_TO`](#date-last-published-to)
- [`DECODE_ENTITIES`](#decode-entities)
- [`DIFFERENCE`](#difference)
- [`DIVIDE`](#divide)
- [`EACH`](#each)
- [`EACH_PAIR`](#each-pair)
- [`EQUAL`](#equal)
- [`FIND`](#find)
- [`FORMAT_DATETIME`](#format-datetime)
- [`GDSN_STRING_WITH_LANGUAGE`](#gdsn-string-with-language)
- [`GDSN_VALUE_WITH_CURRENCY`](#gdsn-value-with-currency)
- [`GDSN_VALUE_WITH_UNIT`](#gdsn-value-with-unit)
- [`GE`](#ge)
- [`GSUB`](#gsub)
- [`GT`](#gt)
- [`IF`](#if)
- [`IN`](#in)
- [`INT`](#int)
- [`IS_VALID_GTIN`](#is-valid-gtin)
- [`ISNUMBER`](#isnumber)
- [`JOIN`](#join)
- [`JOIN_ASSET_VALUES`](#join-asset-values)
- [`JOIN_LOCALIZED_PATH_NAMES`](#join-localized-path-names)
- [`JOIN_PATH_IDS`](#join-path-ids)
- [`JOIN_PATH_NAMES`](#join-path-names)
- [`JOIN_PROPERTIES_FROM_GROUP`](#join-properties-from-group)
- [`JOIN_RELATIONS`](#join-relations)
- [`JOIN_VALUES`](#join-values)
- [`LE`](#le)
- [`LENGTH`](#length)
- [`LET...IN`](#let-in)
- [`LOCALIZED_ASSET_VALUE`](#localized-asset-value)
- [`LOCALIZED_ASSET_VALUES`](#localized-asset-values)
- [`LOCALIZED_PATH_NAME`](#localized-path-name)
- [`LOCALIZED_REFERENCED_ASSET_VALUE`](#localized-referenced-asset-value)
- [`LOCALIZED_REFERENCED_ASSET_VALUES`](#localized-referenced-asset-values)
- [`LOCALIZED_REFERENCED_VALUE`](#localized-referenced-value)
- [`LOCALIZED_REFERENCED_VALUES`](#localized-referenced-values)
- [`LOCALIZED_VALUE`](#localized-value)
- [`LOCALIZED_VALUES`](#localized-values)
- [`LOOKUP`](#lookup)
- [`LOOKUP_FIRST`](#lookup-first)
- [`LOWER`](#lower)
- [`LPAD`](#lpad)
- [`LT`](#lt)
- [`LTRIM`](#ltrim)
- [`MATCHES`](#matches)
- [`MAX`](#max)
- [`MEDIAN`](#median)
- [`MID`](#mid)
- [`MIN`](#min)
- [`MOD`](#mod)
- [`MODIFIED_SINCE_LAST_PUBLISHED_TO`](#modified-since-last-published-to)
- [`MROUNDUP`](#mroundup)
- [`MULTIPLY`](#multiply)
- [`NOT`](#not)
- [`NOW`](#now)
- [`OR`](#or)
- [`PARENT_ID`](#parent-id)
- [`PATH_ID`](#path-id)
- [`PATH_NAME`](#path-name)
- [`PROPER`](#proper)
- [`PROPERTY_FROM_GROUP`](#property-from-group)
- [`PROPERTY_ID_FROM_GROUP`](#property-id-from-group)
- [`PROPERTY_NAME_FROM_GROUP`](#property-name-from-group)
- [`PROPERTY_VALUE_FROM_GROUP`](#property-value-from-group)
- [`PUBLISHED_TO`](#published-to)
- [`REDUCE`](#reduce)
- [`REFERENCE_QUANTITIES`](#reference-quantities)
- [`REFERENCE_QUANTITY`](#reference-quantity)
- [`REFERENCED_ASSET_VALUE`](#referenced-asset-value)
- [`REFERENCED_VALUE`](#referenced-value)
- [`REFERENCED_VALUES`](#referenced-values)
- [`REGEX_MATCHES`](#regex-matches)
- [`RELATION`](#relation)
- [`REPLACE`](#replace)
- [`ROUND`](#round)
- [`RPAD`](#rpad)
- [`RTRIM`](#rtrim)
- [`SENTENCE`](#sentence)
- [`SERIALIZED_DIGITAL_ASSETS`](#serialized-digital-assets)
- [`SLICE`](#slice)
- [`SPLIT`](#split)
- [`SQUARE_ROOT`](#square-root)
- [`SQUISH`](#squish)
- [`STRIP_HTML`](#strip-html)
- [`SUBSTITUTE`](#substitute)
- [`SUBSTITUTE_VALUE`](#substitute-value)
- [`SUBSTRING`](#substring)
- [`SUBTRACT`](#subtract)
- [`TEXT`](#text)
- [`TIME_IN_TIMEZONE`](#time-in-timezone)
- [`TODAY`](#today)
- [`TRANSFORM_ASSET_FORMAT`](#transform-asset-format)
- [`TRANSFORM_ASSET_URL`](#transform-asset-url)
- [`TRANSFORM_ASSET_URLS`](#transform-asset-urls)
- [`TRANSFORM_LOCALIZED_ASSET_URL`](#transform-localized-asset-url)
- [`TRANSPOSE`](#transpose)
- [`UNIQ`](#uniq)
- [`UNIVERSAL_PROPERTIES`](#universal-properties)
- [`UPDATED_AT`](#updated-at)
- [`UPPER`](#upper)
- [`VALUE`](#value)
- [`VALUES`](#values)
- [`VALUE_AT`](#value-at)
- [`WORD_COUNT`](#word-count)

## Function details

### ADD

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Add numbers or dates.

**Syntax**

```text
ADD('{{value}}','{{value}}'...)
```

**Official example**

```text
ADD(VALUE('MSRP'),VALUE('Surcharge')
```

**Output**

`21.99`

### AINDEX

**Compatible with:** Digital Asset Renaming Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

Used in digital asset renaming formulas to add an alphabetical index to an asset name. Define the position in the alphabet (1=A, 2=B, etc) and function will return a series of alphabetical characters for each digital asset.

**Syntax**

```text
{{AINDEX({{numeric_start_position}})}}
```

**Official example**

```text
IMAGE_{{VALUE('Product ID')}}_{{AINDEX(2)}}
```

**Output**

`IMAGE_4060375_B.png, IMAGE_4060375_C.png`

### AND

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Allows testing two values in relation to each other in a formula. Both values must be true for the result to be true. Click here for more information on conditional formulas to achieve a true/false result.

**Syntax**

```text
AND('{{value_or_formula1}}','{{value2_or_formula2}}'...)
```

**Official example**

```text
IF(AND(VALUE('Color'),VALUE('Size')),'Apparel','Hard Goods')
```

**Output**

`Apparel`

### ARRAY_SUM

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Adds together the whole values in an array (ignores remainders after the decimal point) and returns a sum of the whole integers.

**Syntax**

```text
ARRAY_SUM('{{array}}')
```

**Official example**

```text
ARRAY_SUM(VALUES('Component Cost'))
```

**Output**

`93`

### ASSET

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns metadata for an asset. You specify the metadata property, and the position of the asset you want to return the property from (position optional). Function returns the value stored in the metadata property. System metadata properties must be prefixed with salsify:. Click here for the list of Salsify system metadata properties. Click here for more information on digital asset URLs and metadata.

**Syntax**

```text
ASSET('{{digital_asset_metadata_property_id}}',{{optional_index}})
```

**Official example**

```text
ASSET('Photographer')
```

**Output**

`LB Jeffreys`

### ASSET_VALUE

**Compatible with:** Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas

Returns the value of the specified metadata attribute for the Nth (optional) digital asset in the product. If index isn't specified, formula returns value for the first asset. System metadata properties must be prefixed with salsify:. Click here for the list of Salsify system metadata properties. Click here for more information on digital asset URLs and metadata.

**Advanced guide:** [Advanced Formulas & Arrays](salsify-advanced-formulas-arrays.md)

**Syntax**

```text
ASSET_VALUE('{{propertyID}}','{{metadata_attribute}}','{{index}}')
```

**Official example**

```text
ASSET_VALUE('Hero Image', 'salsify:Height', 1)
```

**Output**

`500`

### ASSET_VALUES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns metadata for all digital assets stored in the specified property.

**Syntax**

```text
ASSET_VALUES('{{propertyID}}','{{metadata_attribute}}')
```

**Official example**

```text
ASSET_VALUES('Lifestyle Images','salsify:Filename')
```

**Output**

`lifestyle_image_01.png, lifestyle_image_02.png, lifestyle_image_03.png`

### AT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Allows you to return the Nth value of an array.

**Syntax**

```text
AT(['{{value1}}','{{value2}}','{{value3}}'],{{optional_index}})
```

**Official example**

```text
AT(["Red", "Blue", "White"], 3)
```

**Output**

`White`

### CHANNEL_STATUS_FROM

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns channel status string value for the most recent publish, if it exists. Returns empty/null value if no status is available from the channel, or product has never been published through the channel. To find channel ID, navigate to the channel and the ID is in URL path after /channels/.

Function is not currently available for in-app computed properties.

**Syntax**

```text
CHANNEL_STATUS_FROM('{{channel_id}}')
```

**Official example**

```text
CHANNEL_STATUS_FROM(11234)
```

**Output**

`"Published"`

### CLEAN_TEXT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Removes any special and/or hidden characters, including trademarks and/or copyright symbols. Does not remove common punctuation or line breaks. See the list below for characters that will remain in values. Click here for more information on removing special characters and symbols.

**Syntax**

```text
CLEAN_TEXT(VALUE('{{value}}'))
```

**Official example**

```text
CLEAN_TEXT(VALUE('Brand'))
```

**Output**

`Acme`

### COALESCE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Define multiple inputs (properties and/or string values) in order of priority, and function outputs the first value that's not empty. Click here for more information on how to set a default value and return a value from a set of properties with COALESCE.

**Syntax**

```text
COALESCE('{{value1}}','{{value2}}',...)
```

**Official example 1**

```text
COALESCE(VALUE('eCommerce Name'),VALUE('Product Name'))
```

**Output**

`Titan Wireless Optical Mouse - Multicolor`

**Official example 2**

```text
COALESCE(VALUE('Walmart Name'),'Wireless Mouse')
```

**Output**

`Wireless Mouse`

**Official example 3**

```text
COALESCE(VALUE('Walmart Name'),CONCATENATE(VALUE('Product Name'),' - Optical'))
```

**Output**

`Titan Wireless Mouse - Optical`

### COLLECTION

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Construct a collection by specifying key-value pairs of information. To use, provide an array of objects where the first element is the first key, the second element is that key’s corresponding value, repeated for all key-value pairs of information. Note that null keys and their values will be omitted, but null values will appear in the returned collection.

**Syntax**

```text
COLLECTION('{{key1}}','{{value1}}','{{key2}}','{{value2}}'...)
```

**Official example**

```text
COLLECTION( "Color Family", VALUE("Color"), "Material Name", VALUE("Material"))
```

**Output**

`'{ "Color Family" => "Blue", "Material Name" => "Cotton" }'`

### COMPACT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Removes blank values that would be generated by empty properties. Click here for how to use COMPACT to return a group of values to an attribute.

**Syntax**

```text
COMPACT('{{formula}}')
```

**Official example**

```text
COMPACT(CONCAT_ARRAYS(VALUES('Feature 1'), VALUES('Feature 2'), VALUES('Feature 3')))
```

**Output**

`Output: Blue, 2 pack`

### COMPOUND

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Construct a collection by specifying key-value pairs of information. To use, provide an array of objects where the first element is the first key and the second element is that key’s corresponding value, repeated for all key-value pairs of information.

**Syntax**

```text
COMPOUND('{{key1}}','{{value1}}','{{key2}}','{{value2}}'...)
```

**Official example 1**

```text
COMPOUND("Color Family",VALUE("Color"))
```

**Output**

`'{ "Color Family" => "Blue" }'`

**Official example 2**

```text
COMPOUND("Color Family",VALUE("Color"),"Fabric",VALUE("Material"))
```

**Output**

`'{ "Color Family" => "Blue", "Material Name" => "Cotton" }'`

**Official example 3**

```text
COMPOUND("Color", VALUES("Color"))
```

**Output**

`['{ "Color" => "Blue" }', '{ "Color" => "Green" }']`

### CONCAT_ARRAY

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Combines together two or more arrays. You can concatenate as many arrays as you want, and you can combine literal text values with other Salsify property values. Click here for more information on mapping to an array of multi-value properties.

**Syntax**

```text
CONCAT_ARRAY('{{any_array}}','{{any_array}}'...)
```

**Official example**

```text
CONCAT_ARRAYS(VALUES('Features'), VALUES('Benefits'))
```

**Output**

`Output: shiny, bright, pretty, kind`

### CONCATENATE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Combines together multiple values. You can concatenate as many values as you want, and you can combine literal text values with other Salsify formulas. Click here for more information on how to map to multiple single-value properties.

**Syntax**

```text
CONCATENATE('{{value1}}','{{value2}}',...)
```

**Official example 1**

```text
CONCATENATE('$',VALUE('Retail Price'))
```

**Output**

`$75.0`

**Official example 2**

```text
CONCATENATE('$',VALUE('Retail Price'),' USD')
```

**Output**

`$75.0 USD`

**Official example 3**

```text
CONCATENATE('$',TEXT(VALUE('Retail Price'),'0.00'),'USD')
```

**Output**

`$75.00 USD`

### CONTAINS

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Tests a value for the string specified in the argument. If the string exists in the value, result is true; if not, false.

**Syntax**

```text
CONTAINS('{{value_to_test}}','{{string_to_check}}')
```

**Official example**

```text
IF(CONTAINS(VALUE('Brand'),'Salsify'),'Cool','Bummer')
```

**Output**

`Output: Cool`

### CREATED_AT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Returns the date product record was created, in UTC in the format yyyy-mm-dd.

**Syntax**

```text
CREATED_AT()
```

**Official example**

```text
CREATED_AT()
```

**Output**

`2019-03-29`

### CURRENT_LOCALE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the abbreviation for the locale you're currently using (ie. es-MX).

**Syntax**

```text
CURRENT_LOCALE()
```

**Official example**

```text
CURRENT_LOCALE()
```

**Output**

`fr-FR`

### CURRENT_PROPERTY_ID

**Compatible with:** Digital Asset Renaming Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

Returns the unique ID of the property to which the digital asset is currently linked. Useful when you need to include the internal Salsify property name (e.g., high_res_packaging) in the final exported filename to distinguish between different types of assets associated with the same product.

**Syntax**

```text
CURRENT_PROPERTY_ID()
```

**Official example**

```text
{{VALUE("Product ID")}}_{{CURRENT_PROPERTY_ID()}}_{{CURRENT_PROPERTY_INDEX(1,2)}}
```

**Output**

`0102918_Main_Image_01.png`

### CURRENT_PROPERTY_INDEX

**Compatible with:** Digital Asset Renaming Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

Return the index position of the digital asset within the property that it is linked to. Useful when you have multiple digital assets linked to a single property, and you need to include the index number to create unique filenames.

**Syntax**

```text
CURRENT_PROPERTY_INDEX({{number_start_position}},{{number_characters_to_return}})
```

**Official example**

```text
{{VALUE("Product ID")}}_{{CURRENT_PROPERTY_ID()}}_{{CURRENT_PROPERTY_INDEX(1,2)}}
```

**Output**

`0102918_Main_Image_01.png`

### DATA_INHERITANCE_HIERARCHY_LEVEL

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

If product has a data inheritance hierarchy level, the output is the level's ID.

**Syntax**

```text
DATA_INHERITANCE_HIERARCHY_LEVEL()
```

**Official example**

```text
DATA_INHERITANCE_HIERARCHY_LEVEL()
```

**Output**

`Style`

### DATE_LAST_PUBLISHED_TO

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns date of most recent publish through the channel indicated via the publish button in the channel, through ephemeral publish or marked as a publish event. If product has not been published, result is empty/null. To find channel ID, navigate to the channel and the ID is in URL path after /channels/.

Function is not currently available for in-app computed properties.

**Syntax**

```text
DATE_LAST_PUBLISHED_TO('{{channel_id}}')
```

**Official example**

```text
DATE_LAST_PUBLISHED_TO(11234)
```

**Output**

`2017-05-24`

### DECODE_ENTITIES

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Decode entities in a string into their UTF-8 equivalents.

**Syntax**

```text
DECODE_ENTITIES('{{string}}')
```

**Official example**

```text
DECODE_ENTITIES('Salsify')
```

**Output**

`Salsify`

### DIFFERENCE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Subtract one array from another to return only the remaining values.

**Syntax**

```text
DIFFERENCE('{{array1}}','{{array2}}')
```

**Official example**

```text
DIFFERENCE(['White','Blue','Red'],['Blue','Red'])
```

**Output**

`White`

### DIVIDE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Divides one number by another.

**Syntax**

```text
DIVIDE('{{number1}}','{{number2}}')
```

**Official example**

```text
DIVIDE(VALUE('Cost'),VALUE('Retail')
```

**Output**

`.4`

### EACH

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Access each value in an array. To use, define the array, name for each item within the array, and the action to take on each. Typically used in combination with other formulas. Optionally, include index to add a number corresponding to each item's position in the array.

**Advanced guide:** [Advanced Formulas & Arrays](salsify-advanced-formulas-arrays.md)

**Syntax**

```text
EACH({{'array'}},({{name_for_single_item_in_array}},{{index}}),=>_{{'action_you'd_like_to_take'}})
```

**Official example**

```text
EACH(
VALUES('Bullet Points'), (feature,index) =>

CONCATENATE(
'Bullet ',
index,': ',
feature
)
)
```

**Output**

`Bullet 1: Red, Bullet 2: Blue`

### EACH_PAIR

**Compatible with:** Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas

EACH_PAIR is only available to users with PXM Advance. Access each key-value pair in a collection. To use, define the collection, name for each key and value within the collection, and the action to take on each. Returns an array of results from that action applied to each key-value pair. Typically used in combination with other formulas.

**Syntax**

```text
EACH_PAIR({{collection}}, ( {{key}}, {{value}} ) => {{ action }} )
```

**Official example**

```text
LET collection = COLLECTION("Color", VALUE("Color")) IN

EACH_PAIR(collection, (key, value) => CONCATENATE(key, " is ", value))
```

**Output**

`["Color is Blue"]`

### EQUAL

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Compares two values, and can be used with conditional formulas to evaluate true/false state. Can be used in combination with IF. Returns true if value is equal to the compared value. Click here for more information on using conditional formulas to achieve a true/false result.

**Syntax**

```text
EQUAL('{{value1}}','{{value2_or_number}}')
```

**Official example**

```text
IF(EQUAL(VALUE('Assembly Required?'), 'Yes'), 'Y', 'N')
```

**Output**

`Output: N`

### FIND

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Finds a string of characters inside a specified search location, in most cases a property value or variable. Combine with other formulas to perform actions on found string. Like its Excel counterpart, it returns the numeric location in the string. Typically used as a helper with other functions.

**Syntax**

```text
FIND('{{search_string}}','{{search_location}}')
```

**Official example**

```text
IF(FIND('Soft Line',VALUE('Category')),'Apparel','Hard Goods')
```

**Output**

`Output: Apparel`

### FORMAT_DATETIME

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Transforms a date from one format to another. Where transformed date is not included, default is Salsify format (YYYY-MM-DD). Include the current date value, either fixed or stored, and define the format where %m = month, %d = day, %Y = year. Uses strftime formatting. Include delimiters in the date parameters to define the separate the date parts.

**Syntax**

```text
FORMAT_DATETIME({{'current_date_value'}},{{'current_date_parameters'}},{{'optional_transformed_date_parameters'}})
```

**Official example**

```text
FORMAT_DATETIME(VALUE('Date Property'),'%Y-%m-%d', '%m/%d/%Y')
```

**Output**

`02/26/2019`

### GDSN_STRING_WITH_LANGUAGE

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

GDSN specific formula that adds a language attribute to a string. We recommend using this when GDSN requires the language to be specified. It can also be used for strings that need to be provided in more than one language.

**Syntax**

```text
GDSN_STRING_WITH_LANGUAGE('{{stringValue}}','{{languageCode}}')
```

**Official example**

```text
GDSN_STRING_WITH_LANGUAGE(VALUE('Description'),'en')
```

**Output**

`{"lang": "en", "value": "60W Lightbulb, made of glass and metal."}`

### GDSN_VALUE_WITH_CURRENCY

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

GDSN specific formula that adds a currency code to a value.

**Syntax**

```text
GDSN_VALUE_WITH_CURRENCY('{priceValue}}', '{{currencyCode}}')
```

**Official example**

```text
GDSN_VALUE_WITH_CURRENCY(VALUE('MSRP'), 'USD')
```

**Output**

`{"value": "7.99", "currency": "USD"}`

### GDSN_VALUE_WITH_UNIT

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

GDSN specific formula that adds a measurement unit to a value.

**Syntax**

```text
GDSN_VALUE_WITH_UNIT(‘{{unitValue}}’, unitOfMeasure)
```

**Official example**

```text
GDSN_VALUE_WITH_UNIT(VALUE(‘Depth’), value(‘Depth UOM’))
```

**Output**

`{“value”: “12”, “unitOfMeasure”: “INH”}`

### GE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Greater than or Equal to. Allow you to compare two numbers/numeric values, and can be used with conditional formulas to evaluate true/false state. Can be used in combination with IF. Returns true if value is greater than or equal to the compared value.

**Syntax**

```text
GE('{{value1}}','{{value2_or_number}}')
```

**Official example**

```text
IF(GE(VALUE('Width'),'12'),'Large','Small')
```

**Output**

`Output: Small`

### GSUB

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

For our users familiar with regular expressions, the GSUB function allows full regular expression functionality including back references.

**Syntax**

```text
GSUB('{{value1}}','{{REGEX}}','{{value2}}')
```

**Official example 1**

```text
GSUB('Shiny 123 Shiny','.*?([0-9]+).*', '\\1')
```

**Output**

`123`

**Official example 2**

```text
[^A-Za-z0-9()$!@#%^&*+=_,/\'\":;?\\s\n.-]
```

**Official example 3**

```text
\\D+
```

### GT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Greater than. Compare two numbers to return a true or false answer. Can be used with conditional formulas, and in combination with IF. Returns true if value is greater than the compared value.

**Syntax**

```text
GT('{{value1}}','{{value2_or_specific_value}}')
```

**Official example**

```text
IF(GT(VALUE('Width'),'6'),'Large','Small')
```

**Output**

`Large`

### IF

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs either one value or another, depending on whether test is true or false. true and false outputs can be either literal values or Salsify formulas. This is similar to the IF formula in Excel. Tests either check if a product has a value for a particular property or check whether the value for a product's property is equal to a specific value. Click here for more information on testing for any value.

**Syntax**

```text
IF('{{test_any}}','{{output_if_true}}','{{optional_false_output}}')
```

**Official example 1**

```text
IF(VALUE('Brand'),VALUE('Brand'))
```

**Output**

`Product 1: no value Product 2: Healthy Galaxy`

**Official example 2**

```text
IF(VALUE('Brand'),VALUE('Brand'),'PXM Industries')
```

**Output**

`Formula checks for the existence of a value in the specified location and if one exists, it returns that value. If not, it returns the default text value specified. which is PXM Industries.`

**Official example 3**

```text
IF(EQUAL(VALUE('Brand'),'Healthy Galaxy'),VALUE('Fat (g)'))
```

**Output**

`Product 1: no value Product 2: 11`

### IN

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns T/F for whether searched text exists in the properties/array searched. Click here for more information on testing the existence of specific values in a multi-value property or in an array of single-value properties.

**Syntax**

```text
IN('{{searched_string}}','{{value1}}','{{value2}}',...)
```

**Official example 1**

```text
IN('mouse','technology','electronics','mouse')
```

**Output**

`true`

**Official example 2**

```text
IN('mouse',['technology','electronics','mouse'])
```

**Output**

`[false, false, true]`

**Official example 3**

```text
IN(['technology','electronics','mouse'],'mouse')
```

**Output**

`[false, false, true]`

### INT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Converts a number with fractional parts (digits after the decimal point) to a whole integer with no decimal. No rounding is involved, so for example, 3.2 and 3.9 would both be converted to 3.

**Syntax**

```text
INT({{'numeric'}})
```

**Official example**

```text
INT('3.2')
```

**Output**

`3`

### IS_VALID_GTIN

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Checks for a valid UPC (correct number of digits and valid check digit) or GTIN and returns a true/false value.

**Syntax**

```text
IS_VALID_GTIN({{'property_or_string'}},{{'gtin14_gtin13_gtin12_gtin8_or_upc_'}})
```

**Official example**

```text
IS_VALID_GTIN(VALUE('GTIN'),'gtin12')
```

**Output**

`false`

### ISNUMBER

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Checks whether a value is a number or not. Outputs true if value is a number, otherwise false. Typically used in combination with conditionals like IF.

**Syntax**

```text
ISNUMBER('{{value}}')
```

**Official example**

```text
ISNUMBER('Hello')
```

**Output**

`False`

### JOIN

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Combines all values for a property as a single value with a specified delimiter between them. Use with VALUES rather than VALUE. Click here for more examples using the JOIN formula.

**Syntax**

```text
JOIN('{{value}}','{{delimiter}}')
```

**Official example**

```text
JOIN(VALUES('Bullets'), ';')
```

**Output**

`red;blue`

### JOIN_ASSET_VALUES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Joins all metadata values together as a single value with a delimiter between them for all of the digital assets associated with a property. You can specify the delimiting character or function will use , by default. Click here for more information on using this formula on custom metadata.

**Advanced guide:** [Advanced Formulas & Arrays](salsify-advanced-formulas-arrays.md)

**Syntax**

```text
JOIN_ASSET_VALUES('{{propertyID}}','{{metadata_property}}','{{delimiter}}')
```

**Official example**

```text
JOIN_ASSET_VALUES('Lifestyle Images', 'salsify:Filename', ', ')
```

**Output**

`DSC01.jpg,DSC02.jpg.`

### JOIN_LOCALIZED_PATH_NAMES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Joins all levels of the hierarchy's names for a property's stored locale together as a single value separated by the delimeter specified, and for the property value specified by numeric index. Default delimiter is / and default index is 1. If your hierarchy properties include different value IDs and names, you can use the PATH_ID or JOIN_PATH_ID function to access IDs. Also accepts an array for the index to pull back multiple values.

**Syntax**

```text
JOIN_LOCALIZED_PATH_NAMES('{{property_id}}','{{locale}}','{{optional_delimiter}}','{{depth_index}}','{{position_index}}')
```

**Official example**

```text
JOIN_LOCALIZED_PATH_NAMES('Category', 'fr-FR')
```

**Output**

`Des sacs/Sacs pour ordinateur portable/Sac à dos pour ordinateur portable`

### JOIN_PATH_IDS

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Joins all levels of the hierarchy's IDs for a property's stored locale together as a single value separated by a delimiter, and for the property value specified by numeric index. Default delimiter is / and default index is 1. If your hierarchy properties include different value IDs and names, you can also use the PATH_ID function to access IDs. Also accepts an array for the index to pull back multiple values.

**Syntax**

```text
JOIN_PATH_IDS('{{property_ID}}','{{optional_delimiter}}','{{optional_numeric_index}}')
```

**Official example**

```text
JOIN_PATH_IDS("Category", " | ", 2)
```

**Output**

`Luggage | Wheeled Luggage | Wheeled Carry-on Luggage`

### JOIN_PATH_NAMES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Joins all levels of the hierarchy's names for the property together using delimeter specified, and for the property value specified by numeric index. Default delimiter is / and default index is 1. If your hierarchy properties include different value IDs and names, you can use the PATH_ID and JOIN_PATH_IDSfunction to access IDs. Also accepts an array for the index to pull back multiple values.

**Syntax**

```text
JOIN_PATH_NAMES('{{propertyID}}','{{optional_delimiter}}','{{optional_numeric_index}}')
```

**Official example**

```text
JOIN_PATH_NAMES("Category", " | ", 2)
```

**Output**

`Luggage | Wheeled Luggage | Wheeled Carry-on Luggage`

### JOIN_PROPERTIES_FROM_GROUP

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Localized Properties

Returns all properties as a series of sets of values (property ID, value) with specified separators.

**Syntax**

```text
JOIN_PROPERTIES_FROM_GROUP('{{property_group_name}}','{{optional_separator}}','{{pair_separator}}')
```

**Official example**

```text
JOIN_PROPERTIES_FROM_GROUP('General', ' - ', ', ')
```

**Output**

`Record ID - 123, Record Name - Jetsetter Carry On`

### JOIN_RELATIONS

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Join all product identifiers of targets for a given relation label into a single value with a delimiter between them. Can specify the delimiter - default character is ;.

**Syntax**

```text
JOIN_RELATIONS('{{relation_label}}','{{delimiter}}')
```

**Official example**

```text
JOIN_RELATIONS('Parent/Child', '|')
```

**Output**

`1111|3434|3445|4545`

### JOIN_VALUES

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

For properties with multiple values, combines all of the values together into a single value with delimiters between. Can specify the delimiter - default value is ,.

**Syntax**

```text
JOIN_VALUES('{{propertyID}}','{{delimiter}}')
```

**Official example**

```text
JOIN_VALUES('Feature Bullets', ', ')
```

**Output**

`Big, Shiny, Economical`

### LE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Less than or equal to. Compares two numbers/numeric values, and can be used with conditional formulas like IF to evaluate true/false state. Returns true if value is less than or equal to the compared value.

**Syntax**

```text
LE('{{value1}}','{{value2_or_number}}')
```

**Official example**

```text
LE(VALUE('Width'),'12')
```

**Output**

`true`

### LENGTH

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the number of characters for the specified parameter. If used with VALUE, it returns the number of characters in the value. If used with VALUES or an array of values, it returns the number of values.

**Syntax**

```text
LENGTH('{{value}}')
```

**Official example**

```text
LENGTH(VALUE('Brand'))
```

**Output**

`7`

### LET...IN (language construct)

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Use to define variables to be used in subsequent formulas. Variables can contain fixed values, or can perfom functions. Click here for more information on variables.
Note: When using in templated export templates, don't use the normal SALSIFY_ prefix on IN.

**Detailed guide:** [Variables to Streamline Salsify Formulas](salsify-variables.md)

**Syntax**

```text
let_'{{variable_name}}'='{{value_or_formula}}'_in
```

**Official example**

```text
let x='™' in
let y=VALUE('Brand Name') in

CONCATENATE(y,x)
```

**Output**

`Wildflower™`

### LOCALIZED_ASSET_VALUE

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns the asset metadata of the asset at the given index in the specified locale.

**Syntax**

```text
LOCALIZED_ASSET_VALUE('{{propertyID}}','{{metadata_attribute}}','{{locale}}','{{index}}')
```

**Official example 1**

```text
LOCALIZED_ASSET_VALUE('Lifestyle Images','salsify:Filename','es-MX')
```

**Output**

`lifestyle_image_01.png`

**Official example 2**

```text
LOCALIZED_ASSET_VALUE('Lifestyle Images','salsify:Filename','es-MX',2)
```

**Output**

`lifestyle_image_02.png`

### LOCALIZED_ASSET_VALUES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns all or a subset of the asset's metadata values in the specified locale, starting at the index and continuing until the length value.

**Syntax**

```text
LOCALIZED_ASSET_VALUES('{{propertyID}}','{{metadata_attribute}}','{{locale}}','{{index}}','{{optional_max_values}}')
```

**Official example 1**

```text
LOCALIZED_ASSET_VALUES('Lifestyle Images','salsify:Filename','es-MX')
```

**Output**

`lifestyle_image_01.png`

**Official example 2**

```text
LOCALIZED_ASSET_VALUES('Lifestyle Images','salsify:Filename','es-MX',2,1)
```

**Output**

`lifestyle_image_02.png`

### LOCALIZED_PATH_NAME

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Outputs the Nth hierarchical level of the referenced property's localized name, from top to bottom. Optional index specifies from which property value to return. If index is not included, default behavior returns name from the first value.

**Syntax**

```text
LOCALIZED_PATH_NAME('{{property_id}}','{{locale}}','{{depth_index}}','{{position_index}}')
```

**Official example**

```text
LOCALIZED_PATH_NAME('Category','fr-FR',2)
```

**Output**

`Suppléments de protéines`

### LOCALIZED_REFERENCED_ASSET_VALUE

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

For localized digital asset properties, returns the value of the specified metadata attribute for the Nth (optional) digital asset of the referenced product. Accepts an optional index to define which referenced product to return values from, and an optional index to define which attribute position to return the value from.

**Syntax**

```text
LOCALIZED_REFERENCED_ASSET_VALUE('{{reference_property}}','{{propertyID}}','{{metadata_attribute}}','{{locale}}','{{product_reference_index}}','{{asset_property_index}}')
```

**Official example 1**

```text
LOCALIZED_REFERENCED_ASSET_VALUE('Bundle Products','Lifestyle Images','salsify:Filename','es-MX')
```

**Output**

`lifestyle_image_01.png`

**Official example 2**

```text
LOCALIZED_REFERENCED_ASSET_VALUE('Bundle Products','Lifestyle Images','salsify:Filename','es-MX',2,2)
```

**Output**

`lifestyle_image_03.png`

### LOCALIZED_REFERENCED_ASSET_VALUES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

For localized digital asset properties, returns all values of the specified metadata attribute stored under the specified locale for the referenced product.

**Syntax**

```text
LOCALIZED_REFERENCED_ASSET_VALUES('{{reference_property}}','{{propertyID}}','{{metadata_attribute}}','{{locale}}')
```

**Official example**

```text
LOCALIZED_REFERENCED_ASSET_VALUES('Bundle Products','Lifestyle Images','salsify:Filename','es-MX')
```

**Output**

`lifestyle_image_01.png, lifestyle_image_02.png, lifestyle_image_a.png, lifestyle_image_b.png`

### LOCALIZED_REFERENCED_VALUE

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

This function is compatible with organizations that have the product reference property type enabled, and also have localization enabled. Returns first value from the specified property from the products stored in the specified index position in a reference property.

**Syntax**

```text
LOCALIZED_REFERENCED_VALUE('{{reference_propertyID}}', {{index}},'{{property_from_stored_reference_product}}','{{locale}}')
```

**Official example 1**

```text
LOCALIZED_REFERENCED_VALUE('Bundle Components', 2, 'Bullet Points','fr-CA')
```

**Output**

`collation propre et sain`

**Official example 2**

```text
LOCALIZED_REFERENCED_VALUE('Bundle Components', 2, 'salsify:universal:universal_bullet_points,'fr-CA')
```

**Output**

`collation propre et sain`

### LOCALIZED_REFERENCED_VALUES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns values from all products stored in a reference property in the locale you specify. You choose the reference property, property to pull values from and the locale to return values for. By default, all values are returned from all products in the specified reference property. You can add an optional index to return a single value from each product in a specific position.

**Syntax**

```text
LOCALIZED_REFERENCED_VALUES('{{reference_property}}', {{property_from_stored_reference_product}}, {{locale}}, {{optional_index}})
```

**Official example 1**

```text
LOCALIZED_REFERENCED_VALUES('Bundle Components','Tags','es-MX')
```

**Output**

`soleado lentes Gafas de sol pelucas disfraz pelo gabardina Saco sigilo`

**Official example 2**

```text
LOCALIZED_REFERENCED_VALUES('Bundle Components','Tags','es-MX',2)
```

**Output**

`lentes disfraz Saco`

**Official example 3**

```text
LOCALIZED_REFERENCED_VALUES('Bundle Components', 'salsify:universal:universal_tags','es-MX')
```

**Output**

`soleado lentes Gafas de sol pelucas disfraz pelo gabardina Saco sigilo`

### LOCALIZED_VALUE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

For localized properties, returns the value stored in the locale you specify.

**Syntax**

```text
LOCALIZED_VALUE('{{reference_property}}','{{locale}}', {{index}})
```

**Official example 1**

```text
LOCALIZED_VALUE('Bullet Points','fr-CA')
```

**Output**

`Peut être lavé à la main et séché en ligne`

**Official example 2**

```text
LOCALIZED_VALUE('Bullet Points','fr-CA',2)
```

**Output**

`Durable, confortable et léger`

**Official example 3**

```text
LOCALIZED_VALUE('salsify:universal:universal_bullet_points', 'fr-CA')
```

**Output**

`unisex`

### LOCALIZED_VALUES

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Returns specified values from a property in the localized language chosen. You can specify which value to start with, and a maximum number of values to return. Default behavior is to return all values for the specified locale.

**Syntax**

```text
LOCALIZED_VALUES('{{propertyID}}'}}'{{locale}}'}}{{optional_index}}}}{{optional_max_values}})
```

**Official example 1**

```text
LOCALIZED_VALUES('Tags','es-MX')
```

**Output**

`té, desayuno, energía'`

**Official example 2**

```text
LOCALIZED_VALUES('Tags','es-MX',2,1)
```

**Output**

`desayuno`

**Official example 3**

```text
LOCALIZED_VALUE('salsify:universal:universal_bullet_points', 'es-MX')
```

**Output**

`té, desayuno, energía'`

### LOOKUP

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Looks up the value for a specified property, references a table stored either in a Salsify digital asset or a publicly accessible URL (e.g., public SFTP location), and returns the corresponding value from the table. Table contains all the allowed values for the property in column A.

**Advanced guide:** [Advanced Formulas & Arrays](salsify-advanced-formulas-arrays.md)

**Syntax**

```text
LOOKUP('{{value}}','{{url_or_asset_ID}}','{{column_header_to_return}}','{{optional_default_value}}')
```

**Official example 1**

```text
LOOKUP(VALUE('Category'),

'https://salsify.exavault.com/p/Enablement/Wildflower-categories.xlsx',

'SuperWidgets Category',

'General')
```

**Output**

`Grocery`

**Official example 2**

```text
LOOKUP(VALUE('Category'),

'ae3314e7a44442ca98489faf82e911dc5152c945',

'SuperWidgets Category',

'General')
```

**Output**

`Grocery`

### LOOKUP_FIRST

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Looks up the value for a specified property, references a table stored in an FTP location or a Salsify asset ID and returns the first corresponding value from the table. Table contains all the allowed values for the property in column A.

**Syntax**

```text
LOOKUP_FIRST('{{value}}','{{url_or_asset_ID}}','{{2nd_column_header}}','{{default_value}}')
```

**Official example 1**

```text
LOOKUP_FIRST(
VALUE('Category'),
'http://salsify.exavault.com/p/Enablement/Wildflower-categories.xlsx',
'SuperWidgets',
'General'
)
```

**Output**

`Grocery`

**Official example 2**

```text
LOOKUP_FIRST(
VALUE('Category'),
'ae3314e7a44442ca98489faf82e911dc5152c945',
'SuperWidgets',
'General'
)
```

**Output**

`Grocery`

### LOWER

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Converts the given value into all lowercase.

**Syntax**

```text
LOWER('{{value}}')
```

**Official example**

```text
LOWER(VALUE('Brand')
```

**Output**

`healthy galaxy`

### LPAD

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs a value that is N characters long by adding the specified character to the beginning of the value. Click here for a video example.

**Syntax**

```text
LPAD('{{value}}','{{character_to_pad_with}}',{{number}})
```

**Official example**

```text
LPAD(VALUE('UPC'), '0', '14')
```

**Output**

`00000987654321`

### LT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Less than. Compares two numbers/numeric values, and can be used with conditional formulas like IF to evaluate true/false state. Returns true if value is less than the compared value.

**Syntax**

```text
LT('{{value1}}','{{value2_or_number}}')
```

**Official example**

```text
LT(VALUE('Width'),'6')
```

**Output**

`Output: False`

### LTRIM

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Retains number of characters specified, starting from the left. Trims any additional characters at the right end of the string. LEFT can also be used to perform the same function.

**Syntax**

```text
LTRIM('{{value}}',{{number}})
```

**Official example**

```text
LTRIM(VALUE('UPC'), 11)
```

**Output**

`98765432100`

### MATCHES

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Finds a string of characters inside a specified search location, in most cases a property value or variable. Search string accepts REGEX. Combine with other formulas to perform actions on found string.

**Array behavior:** Returns every match as an array. Passing `MATCHES` directly as an `IF` test can apply the true result once per match and produce duplicate labels. When the requirement is one label if any match exists, scalarize the match array first, for example:

```text
IF(JOIN(MATCHES(bigstring,'bronze|brown|cognac'),''),'Brown')
```

An outer `UNIQ` may not remove duplicates nested inside a matcher result; scalarize before `IF` rather than depending on downstream deduplication.

**Syntax**

```text
MATCHES('{{text_to_search}}',''{{search_string_or_regex}}')
```

**Official example**

```text
MATCHES('I have $5.98 and you have $2.54', '\\$\\d+\\.\\d{2}')
```

**Output**

`Returns, $5.98, $2.55`

### MAX

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the largest numeric values for selected properties.

**Syntax**

```text
MAX('{{value1}}','{{value2}}'...)
```

**Official example**

```text
MAX(VALUE('Length'),VALUE('Width'),VALUE('Height'))
```

**Output**

`10`

### MEDIAN

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the numeric value closest to the average for selected properties.

**Syntax**

```text
MEDIAN('{{value1}}','{{value2}}'...)
```

**Official example**

```text
MEDIAN(VALUE('Length'),VALUE('Width'),VALUE('Height'))
```

**Output**

`5`

### MID

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs a substring of a value starting at the Nth character and continuing for length of characters specified. Similar to MID in Excel.

**Syntax**

```text
MID('{{propertyID}}',{{number_character}},{{string_length}})
```

**Official example**

```text
PROPER(MID(VALUE('Feature Bullet'),9,22))
```

**Output**

`Padded Shoulder Straps`

### MIN

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the smallest numeric values for selected properties.

**Syntax**

```text
MIN('{{value1}}','{{value2}}'...)
```

**Official example**

```text
MIN(VALUE('Length'),VALUE('Width),VALUE('Height'))
```

**Output**

`2`

### MOD

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the remainder when the value is divided by the divisor.

**Syntax**

```text
MOD('{{number}}','{{divisor_number}}')
```

**Official example**

```text
MOD('158','10')
```

**Output**

`8.0`

### MODIFIED_SINCE_LAST_PUBLISHED_TO

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns true/false for whether any property value for the product has been modified since the most recent publish through the channel indicated. To find channel ID, navigate to the channel and the ID is in URL path after /channels/.

**Syntax**

```text
MODIFIED_SINCE_LAST_PUBLISHED_TO('{{channel_id}}')
```

**Official example**

```text
MODIFIED_SINCE_LAST_PUBLISHED_TO(11234)
```

**Output**

`true`

### MROUNDUP

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the value rounded up by a given multiple.

**Syntax**

```text
MROUNDUP('{{propertyID}}',{{multiple_number}})
```

**Official example**

```text
MROUNDUP(VALUE('Price'),5)
```

**Output**

`15.0`

### MULTIPLY

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Multiply numbers or dates.

**Syntax**

```text
MULTIPLY('{{number1}}','{{c2}}'...)
```

**Official example**

```text
MULTIPLY(VALUE('Retail Price'),VALUE('Margin'))
```

**Output**

`15.992`

### NOT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns the reversed logical value. Typically used in combination with other conditional or numeric formulas.

**Syntax**

```text
NOT('{{value1}}','{{value2}}'...)
```

**Official example**

```text
IF(NOT(EQUAL(VALUE('Proposition 65 Warning?'),'No')),'Yes')
```

**Output**

`No`

### NOW

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs the current time in iso8601 format by default (yyyy-mm-ddThh:mm:ss+timezone offset from UTC). Use strftime directives to modify format. Where current time is 10:00 AM on August 8, NOW() returns 2018-08-14T15:00:00+00:00

**Time-zone reference:** [Accepted Salsify Time Zone Names](salsify-time-zones.md)

**Syntax**

```text
NOW('{{optional_format}}')
```

**Official example**

```text
NOW('%D')
```

**Output**

`08/14/18`

### OR

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns TRUE if any of its arguments are TRUE; returns FALSE if all are FALSE.

**Syntax**

```text
OR('{{value1_number1_string1_or_formula1}}','{{value2_number2,_string2_or_formula2}}')
```

**Official example**

```text
IF(OR(EQUAL(VALUE('Category'),'Food'),EQUAL(VALUE('Category'),'Beverage')),'Healthy Galaxy')
```

**Output**

`Healthy Galaxy`

### PARENT_ID

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

If product has a parent, outputs the parent product's ID.

**Syntax**

```text
PARENT_ID()
```

**Official example**

```text
PARENT_ID()
```

**Output**

`Output: JET334`

### PATH_ID

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

For enumerated values with hierarchies, function returns the property value ID in the hierarchy level you specify. Use the optional numeric index in cases where you have multiple values stored and want to return other than the first property value. If index is not included, function will pull from the first property value stored.

**Syntax**

```text
PATH_ID('{{propertyID}}',optional_numeric_depth,{{optional_numeric_index}})
```

**Official example**

```text
PATH_ID('Category',3,2)
```

**Output**

`Hard-side Luggage`

### PATH_NAME

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

For enumerated values with hierarchies, this function returns the property value name in the hierarchy level you specify. Use the optional numeric index in cases where you have multiple values stored and want to return other than the first property value. If index is not included, the function will pull from the first property value stored.

**Syntax**

```text
PATH_NAME('{{propertyID}}',optional_numeric_depth,{{optional_numeric_index}})
```

**Official example 1**

```text
PATH_NAME('Category')
```

**Output**

`Housewares`

**Official example 2**

```text
PATH_NAME('Category',3,2)
```

**Output**

`Hard-side Luggage`

### PROPER

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Capitalizes the first letter of each word in the value.

**Syntax**

```text
PROPER('{{value}}')
```

**Official example**

```text
PROPER(VALUE('Brand')
```

**Output**

`Healthy Galaxy`

### PROPERTY_FROM_GROUP

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns the property and property value at the specified index of a property group with a custom separator applied if provided.

**Syntax**

```text
PROPERTY_FROM_GROUP('{{property_group_name}}',{{index}})
```

**Official example**

```text
PROPERTY_FROM_GROUP('General', ' - ', 2)
```

**Output**

`Record Name`

### PROPERTY_ID_FROM_GROUP

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns the property id at the specified index of the property group.

**Syntax**

```text
PROPERTY_ID_FROM_GROUP('{{property_group_name}}',{{index}})
```

**Official example**

```text
PROPERTY_ID_FROM_GROUP('General')
```

**Output**

`Brand`

### PROPERTY_NAME_FROM_GROUP

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns the property name at the specified index of the property group.

**Syntax**

```text
PROPERTY_VALUE_FROM_GROUP('{{property_group_name}}',2)
```

**Official example**

```text
PROPERTY_NAME_FROM_GROUP('General')
```

**Output**

`Brand Name`

### PROPERTY_VALUE_FROM_GROUP

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns the property value at the specified index of the property group. Typically used where packaging hierarchies are stored.

**Syntax**

```text
PROPERTY_VALUE_FROM_GROUP('{{property_group_name}}',{{index}})
```

**Official example**

```text
PROPERTY_VALUE_FROM_GROUP('General', 2)
```

**Output**

`Jetsetter Carry On`

### PUBLISHED_TO

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns true/false for whether the product has been published through the channel indicated via the publish button in the channel, through ephemeral publish or marked as a publish event. To find channel ID, navigate to the channel and the ID is in URL path after /channels/.

Function is not currently available for in-app computed properties.

**Syntax**

```text
PUBLISHED_TO('{{channel_id}}')
```

**Official example**

```text
PUBLISHED_TO(11234)
```

**Output**

`true`

### REDUCE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

REDUCE allows you to combine the values in an array one by one. You provide the array and a formula that will be run for each value in the array along with the previous result for that formula.

**Syntax**

```text
REDUCE([array],{{formula}},[optional_initial_value])
```

**Official example**

```text
REDUCE([1, 2, 3], (sum, number) => ADD(sum, number))
```

**Output**

`6`

### REFERENCE_QUANTITIES

**Compatible with:** Computed Property Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

For quantified product reference properties, return an array of the quantities for all products stored in the property. To return a single quantity, see REFERENCE_QUANTITY.

**Syntax**

```text
REFERENCE_QUANTITIES('{{reference_property}}')
```

**Official example**

```text
REFERENCE_QUANTITIES('Bundle Components')
```

**Output**

`3 2 1`

### REFERENCE_QUANTITY

**Compatible with:** Computed Property Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

For products referenced in the property, returns the quantity of the specified product. To return quantities for multiple products in a property, see REFERENCE_QUANTITIES.

**Syntax**

```text
REFERENCE_QUANTITY('{{property}}'}}'{{index}}')
```

**Official example 1**

```text
REFERENCE_QUANTITY('Bundle Component')
```

**Output**

`1`

**Official example 2**

```text
REFERENCE_QUANTITY('Bundle Component',2)
```

**Output**

`2`

### REFERENCED_ASSET_VALUE

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns the value of the metadata attribute for the Nth digital asset in the property of the referenced product.

**Syntax**

```text
REFERENCED_ASSET_VALUE('{{reference-property}}', '{{asset_property_from_stored_reference_product}}', '{{metadata_attribute}}',{{product_reference_optional_index}},{{optional_index}})
```

**Official example 1**

```text
REFERENCED_ASSET_VALUE('Brand','Stack Logo','Designer')
```

**Output**

`John Smith (Healthy image 1, designer 1)`

**Official example 2**

```text
REFERENCED_ASSET_VALUE('Brand','Stack Logo','Designer',1,2)
```

**Output**

`Gracie (healthy image 2, designer 1)`

**Official example 3**

```text
REFERENCED_ASSET_VALUE('Brand','Stack Logo','Designer',2,1)
```

**Output**

`Stealth Designer 1`

### REFERENCED_VALUE

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Function works with the Product Reference property type. Allows you to return a property value from a product stored as a value in a reference property type. All properties stored with the referenced product are available to the formula.

**Syntax**

```text
REFERENCED_VALUE('{{property_id_stored_in}}'}}'{{index}}}}'{{property_id_from_stored_product}}'}}{{optional_value_index}}')
```

**Official example 1**

```text
REFERENCED_VALUE('Replacement Parts',1,'Retail Price')
```

**Output**

`19.99`

**Official example 2**

```text
REFERENCED_VALUE('Replacement Parts', 1, 'salsify:universal:universal_retail_price')
```

**Output**

`19.99`

### REFERENCED_VALUES

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns values from all products stored in a reference property. You specify the reference property the products are stored in, and property on that product to return the values from. By default, all values store with the referenced product are returned from all products in the property. You can add an optional index to return values from a specific position for each product. Note that you can specify any property stored on the referenced product.

**Syntax**

```text
REFERENCED_VALUES('{{reference_property}}'}}'{{property_to_return_values_from'}}'}}'{{optional_index}}')
```

**Official example 1**

```text
REFERENCED_VALUES('Bundle Components','Tags')
```

**Output**

`glasses sunglasses wigs disguise hair trenchcoat coat stealth`

**Official example 2**

```text
REFERENCED_VALUES('Bundle Components','Tags',2)
```

**Output**

`glasses, disguise, coat`

**Official example 3**

```text
REFERENCED_VALUE('Bundle Components', 'salsify:universal:universal_tags')
```

**Output**

`sunny, glasses, sunglasses, wigs, disguise, hair, trenchcoat, coat, stealth`

### REGEX_MATCHES

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

For our users familiar with regular expressions, the REGEX_MATCHES function uses a regular expression to extract matching text from a longer string.

**Array behavior:** Returns every regex match as an array. Passing `REGEX_MATCHES` directly as an `IF` test can apply the true result once per match and produce duplicate labels. When the requirement is one label if any match exists, scalarize the match array first, for example:

```text
IF(JOIN(REGEX_MATCHES(bigstring,'bronze|brown|cognac'),''),'Brown')
```

An outer `UNIQ` may not remove duplicates nested inside a matcher result; scalarize before `IF` rather than depending on downstream deduplication.

**Syntax**

```text
REGEX_MATCHES('{{value_to_search}}','{{search_string_or_regex}}')
```

**Official example 1**

```text
REGEX_MATCHES('I have $5.98 and you have $2.54', '\\$\\d+\\.\\d{2}')
```

**Official example 2**

```text
Output:Returns

$5.98

$2.54
```

### RELATION

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Returns product ID of target for a given relation label.

**Syntax**

```text
RELATION('{{relation_label}}',{{optional_index_number}})
```

**Official example**

```text
RELATION('Other Colors',1)
```

**Output**

`11223`

### REPLACE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

For our users familiar with regular expressions, the REPLACE function is just like SUBSTITUTE except it uses a regular expression.

**Syntax**

```text
REPLACE('{{value}}','{{find_text}}','{{replacement_text}}')
```

**Official example**

```text
REPLACE("Shiny 123 Shiny","[0-9]", "")
```

**Output**

`Shiny Shiny`

### ROUND

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Rounds numeric values to the specified number of decimal places.

**Syntax**

```text
ROUND(VALUE('{number}}'),{{number_decimal_places}})
```

**Official example**

```text
ROUND(VALUE('Cost'), 2)
```

**Output**

`19.99`

### RPAD

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs a value of a specified length by adding a number of specified characters at the end of the value.

**Syntax**

```text
RPAD('{{value}}',{{number_padding}},{{number_length}})
```

**Official example**

```text
RPAD(VALUE('Retail Price'),'0',5)
```

**Output**

`75.00`

### RTRIM

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs the specified number of characters from the end of the value. RIGHT can also be used to perform the same function

**Syntax**

```text
RTRIM('{{value}}',{{number}})
```

**Official example**

```text
RTRIM(VALUE('UPC'), 11)
```

**Output**

`76543210000`

### SENTENCE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Capitalizes the first letter of the first word in a string and makes the rest lower case.

**Syntax**

```text
SENTENCE('{{value}}')
```

**Official example**

```text
SENTENCE(VALUE('Warranty')
```

**Output**

`Ten year limited warranty.`

### SERIALIZED_DIGITAL_ASSETS

**Compatible with:** Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas

Returns digital asset metadata for the specified property serialized as JSON

**Syntax**

```text
SERIALIZED_DIGITAL_ASSETS('{{property_id}}')
```

**Official example**

```text
SERIALIZED_DIGITAL_ASSETS('Main Image')
```

**Output**

`{:"salsify:id"=>"c232473f74f6e16ed1d239bf6cf5cf50b3e25173", :"salsify:name"=>"shutterstock_380042722", :"salsify:created_at"=>Sun, 28 Feb 2016 00:11:30 UTC +00:00, :"salsify:updated_at"=>Thu, 25 Jan 2018 18:09:43 UTC +00:00, :"salsify:status"=>:completed, :"salsify:asset_height"=>2579, :"salsify:asset_width"=>3869, :"salsify:asset_resource_type"=>"image", :"salsify:filename"=>"shutterstock_380042722.jpg", :"salsify:bytes"=>2768247, :"salsify:format"=>"jpg", :"salsify:etag"=>"9fc062b0af4baa3d36d1bbbd519aecc9", :"salsify:system_id"=>SalsifyUuid(s-5941e09e-f8ce-4820-a7b9-bdbf6f13d45e), "Manufacturer"=>"Wildflower Imports, Inc."}`

### SLICE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Takes a section/subset of an array. Note that SLICE takes an array and gives you a smaller (or equal size) array in return.

**Syntax**

```text
SLICE('{{value}}','{{number_start_position}}','{{number_values_to_return}}')
```

**Official example**

```text
SLICE(VALUES('Features'), 2, 2)
```

**Output**

`Limited Lifetime Warranty Made in the USA.`

### SPLIT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Separates a single value into multiple values, using a specified charcter as the separator/delimiter.

**Syntax**

```text
SPLIT('{{value1}}','{{delimiting_character}}')
```

**Official example**

```text
SPLIT(VALUE('Bullets'), ',')
```

**Output**

`1 Year Warranty, Made in USA, 80% post-consumer recycled materials`

### SQUARE_ROOT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Calculates the square root of the specified value. Accepts values stored in properties and string values.

**Syntax**

```text
SQUARE_ROOT('{{number}}')
```

**Official example**

```text
SQUARE_ROOT(VALUE('Package Width'))
```

**Output**

`8`

### SQUISH

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs value with all leading and trailing whitespace removed, and any extra whitespace inside the value condensed to a single space.

**Syntax**

```text
SQUISH('{{value}}')
```

**Official example**

```text
SQUISH(VALUE('Description'))
```

**Output**

`This is the description.`

### STRIP_HTML

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Removes all HTML markup and leaves just the regular text.

**Syntax**

```text
STRIP_HTML('{{value}}')
```

**Official example**

```text
STRIP_HTML(VALUE('Description'))
```

**Output**

`My New Product This product fixes all ills!...`

### SUBSTITUTE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Searches for a string in a value and replaces it with what's defined. Can do multiple subsitutions with the same formula by adding comma-separated pairs of find, replace strings.

**Syntax**

```text
SUBSTITUTE('{{value}}','{{find_text}}','{{replace_text}}')
```

**Official example**

```text
SUBSTITUTE(VALUE('Product Description'), '•', '','™','')
```

**Output**

`Durable and lightweight with Velcro closure`

### SUBSTITUTE_VALUE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Searches for a string in a value and replaces it with what's defined in a value pair of find and replace text. Unlike SUBSTITUTE, it cannot handle multiple value pairs.

**Syntax**

```text
SUBSTITUTE_VALUE('{{propertyID}}','{{find_text}}','{{replace_text}}')
```

**Official example**

```text
SUBSTITUTE_VALUE('Product Description', '•', '')
```

**Output**

`Durable and Lightweight`

### SUBSTRING

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Similar to MID in Excel. Outputs a substring of a value starting at the Nth character and continuing for length of characters specified.

**Syntax**

```text
SUBSTRING('{{value}}',{{number_character}},{{string_length}})
```

**Official example**

```text
PROPER(SUBSTRING(VALUE('Feature Bullet'),9,23))
```

**Output**

`Padded Shoulder Straps`

### SUBTRACT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Subtracts one number or date from another.

**Syntax**

```text
SUBTRACT('{{value}}','{{values_or_numeric_value}}'...)
```

**Official example**

```text
SUBTRACT(VALUE('MSRP'),'2')
```

**Output**

`17.99`

### TEXT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Reformats numeric values, stored as text, with specified format. Include decimal even when returning only whole numbers (ie. to return two digit places like 01, format should be 00.) Does not work for values stored as a number or sent to a retailer as a number attribute type.

**Syntax**

```text
TEXT('{{propertyID}}','{{format}}')
```

**Official example**

```text
TEXT(VALUE('MSRP'), '0.00')
```

**Output**

`19.99`

### TIME_IN_TIMEZONE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Converts the given time to the specified timezone. Result is returned in is8601 format (yyyy-mm-ddThh:mm:ss+timezone offset from UTC).

**Time-zone reference:** [Accepted Salsify Time Zone Names](salsify-time-zones.md)

**Syntax**

```text
TIME_IN_TIMEZONE('{{time_to_convert}}'}}'{{input_timezone}}'}}'{{output_timezone}}')
```

**Official example**

```text
TIME_IN_TIMEZONE('2019-08-28T01:56:41+00:00','Eastern Time (US & Canada)','Lisbon')
```

**Output**

`2019-08-28T06:56:41+00:00`

### TODAY

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns today's date based on Coordinated Universal Time (UTC). Used in combination with date information to evaluate IF statements. Useful for date-based product status.

**Syntax**

```text
TODAY()
```

**Official example**

```text
TODAY()
```

**Output**

`2019-04-24`

### TRANSFORM_ASSET_FORMAT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Changes the file extension for a Salsify digital asset URL to specified format. Use in combination with TRANSFORM_ASSET_URL(s) formulas to apply tranformations that change file dimensions or other digital asset attributes. Can be applied to an array of digital asset URLs.

**Syntax**

```text
TRANSFORM_ASSET_FORMAT('{{value_or_string}}','{{format}}','{{optional_index}}')
```

**Official example**

```text
TRANSFORM_ASSET_FORMAT('Main Image', 'png')
```

**Output**

`http://salsify.com/image.png.`

### TRANSFORM_ASSET_URL

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Inserts transformation string in a single Salsify URL to change the size or other characteristics of an image. See the Images Transformation Cheat Sheet for available transformations. To tranform multiple assets, see TRANSFORM_ASSET_URLS. To also transform file type/format, see TRANSFORM_ASSET_FORMAT.

**Syntax**

```text
TRANSFORM_ASSET_URL('{{value_or_string}}','{{transformation_string}}','{{optional_index}}')
```

**Official example**

```text
TRANSFORM_ASSET_URL('Main Image', 'c_fit,w_2000,h_2000',2)
```

**Output**

`0`

### TRANSFORM_ASSET_URLS

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Inserts transformation string for one or more Salsify URLs to change the size or other characteristics of an image. See Transforming Image Files for available transformations. To also transform file type/format, see TRANSFORM_ASSET_FORMAT.

**Syntax**

```text
TRANSFORM_ASSET_URLS('{{propertyID_or_string}}','{{transformation_string}}','{{optional_index}}')
```

**Official example**

```text
TRANSFORM_ASSET_URLS('Additional Product Images', 'c_fit,w_2000,h_2000',2)
```

**Output**

`0`

### TRANSFORM_LOCALIZED_ASSET_URL

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Inserts transformation string in a single Salsify URL to change the size or other characteristics of a localized image. See the Images Transformation Cheat Sheet for available transformations. To transform an unlocalized asset, see TRANSFORM_ASSET_URL. To transform multiple assets, see TRANSFORM_ASSET_URLS. To also transform file type/format, see TRANSFORM_ASSET_FORMAT.

**Syntax**

```text
TRANSFORM_LOCALIZED_ASSET_URL('{{property_ext_id}}', '{{transformation_formula}}', '{{locale_ext_id}}', {{index}})
```

**Official example**

```text
TRANSFORM_LOCALIZED_ASSET_URL("Additional Images", "c_fit,w_2000,h_2000", "en-US", 2)
```

**Output**

`https://images.salsify.com/image/upload/s--FBWvKgIJ--/c_fit,w_2000,h_2000/jqqiuzl3oh6w2lz7bwae.jpg`

### TRANSPOSE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

An array of values is returned as separate values. Where multiple arrays are included, formula returns an array of values from each position in the arrays. Accepts a single array, or a nested array of arrays.

**Syntax**

```text
TRANSPOSE([{{array}}],[{{additional_optional_arrays}}]])
```

**Official example**

```text
TRANSPOSE([['blue','green','yellow'],[4,5,6]])
```

**Output**

`["blue","4"], ["green","5"],, ["yellow","6"]`

### UNIQ

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Removes duplicate values in array, returning only the unique values. Accepts an array of arrays, It will take an array of arrays, but only de-dupes the full array against another full array.

**Syntax**

```text
UNIQ(['value1','value2','value3'...])
```

**Official example**

```text
UNIQ(['Red','Green','Red'])
```

**Output**

`Red, Green`

### UNIVERSAL_PROPERTIES

**Compatible with:** Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas

UNIVERSAL_PROPERTIES is only available to users with PXM Advance. Evaluates an entire universal property collection, returning only collections that contain values. When provided a universal property instead of a collection, returns just the corresponding values if any exist. Note that properties must be mapped to universal properties for values to be returned, an empty collection will be returned when there are no corresponding mappings.

Note that unlike the `VALUES` functions, the ‘salsify:universal:’ prefix is not required. The `UNIVERESAL_PROPERTIES` function only requires the end collection name (i.e. ‘nutritionFacts’).

**Syntax**

```text
UNIVERSAL_PROPERTIES('{{universal_property_collection}}')
```

**Official example 1**

```text
UNIVERSAL_PROPERTIES('fabric')
```

**Output**

`'{ "color" => ["Blue"], "material" => ["Cotton"] }'`

**Official example 2**

```text
UNIVERSAL_PROPERTIES('fabric.color')
```

**Output**

`["Blue"]`

### UPDATED_AT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Digital Asset Renaming Formulas

Returns the date of most recent product record update to any property, in UTC, format yyyy-mm-dd.

**Syntax**

```text
UPDATED_AT()
```

**Official example**

```text
UPDATED_AT()
```

**Output**

`2019-02-26`

### UPPER

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Converts the given value into all uppercase.

**Syntax**

```text
UPPER('{{value}}')
```

**Official example**

```text
UPPER(VALUE('Brand'))
```

**Output**

`HEALTHY GALAXY`

### VALUE

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Outputs value of the given property. If the property has multiple values, it returns only one. Specify a number index to return the value from that position.

**Syntax**

```text
VALUE('{{propertyID}}',{{optional_index}})
```

**Official example 1**

```text
VALUE('Tags')
```

**Output**

`messenger bag`

**Official example 2**

```text
VALUE('Tags',2)
```

**Output**

`unisex`

**Official example 3**

```text
CONCATENATE('This ',VALUE('Tags'),' is made of ',VALUE('Tags',3))
```

**Output**

`This messenger bag is made of vintage leather`

**Official example 4**

```text
VALUE("salsify:universal:universal_tags", 2)
```

**Output**

`unisex`

### VALUES

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Returns all or a subset of the property's property values starting at the index and continuing until the length value. Accepts optional index, which defines from which position to start returning values, and optional maximum number of values to return.

**Syntax**

```text
VALUES('{{propertyID}}','{{optional_index}}','{{optional_number}}')
```

**Official example 1**

```text
VALUES('Tags')
```

**Output**

`windshield, car, bulletproof, shatter-resistant, anti-glare`

**Official example 2**

```text
VALUES('Tags',2)
```

**Output**

`car, bulletproof, shatter-resistant, anti-glare`

**Official example 3**

```text
VALUES('Tags',2,3)
```

**Output**

`car, bulletproof, shatter-resistant`

**Official example 4**

```text
VALUES('Tags',1,4)
```

**Output**

`windshield, car, bulletproof, shatter-resistant`

**Official example 5**

```text
VALUES("salsify:universal:universal_tags", 2)
```

**Output**

`car, bulletproof, shatter-resistant, anti-glare`

### VALUE_AT

**Compatible with:** Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas

VALUE_AT is only available to users with PXM Advance. Returns the value of a collection by its key if a value exists.

**Syntax**

```text
VALUE_AT({{collection}}, {{key}})
```

**Official example**

```text
LET collection = COLLECTION("Color", VALUE("Color")) IN

VALUE_AT(collection, "Color")
```

**Output**

`"Blue"`

### WORD_COUNT

**Compatible with:** Computed Property Formulas; In-app Bulk Edit Formulas; Salsibot Product Edit via Formulas; Digital Asset Renaming Formulas; Templated Export Formulas; Readiness Report Formulas

**Not compatible with:** None

Counts the number of times one word or phrase appears within a text string. Does not accept arrays. Not case sensitive.

**Syntax**

```text
WORD_COUNT('{{string_to_count}}','{{string_to_search}}')
```

**Official example**

```text
WORD_COUNT('love',VALUE('Description'))
```

**Output**

`3`
