# Salsify Advanced Formulas & Arrays

Source: Salsify "Advanced Formulas & Arrays"
Source last modified: May 27, 2025
Extracted: July 30, 2026

**Related guides:** [Variables](salsify-variables.md) | [Function reference](salsify-functions.md) | [Common use cases](salsify-common-use-cases.md)

> **Version note:** This article predates the June 2026 Formulas Cheat Sheet. Use the newer function reference as the authority when syntax or compatibility differs.

**Documented functions used:** [`ADD`](salsify-functions.md#add), [`ASSET_VALUE`](salsify-functions.md#asset-value), [`CONCATENATE`](salsify-functions.md#concatenate), [`EACH`](salsify-functions.md#each), [`IF`](salsify-functions.md#if), [`JOIN`](salsify-functions.md#join), [`JOIN_ASSET_VALUES`](salsify-functions.md#join-asset-values), [`LOOKUP`](salsify-functions.md#lookup), [`VALUE`](salsify-functions.md#value), [`VALUES`](salsify-functions.md#values)

**Legacy or alias name appearing in this article:** `CONCAT`. It does not have a standalone entry in the extracted June 2026 cheat sheet; that sheet documents `CONCATENATE` and `CONCAT_ARRAY`.

## Quick index

- [Working with Variables](#working-with-variables)
- [Working with Arrays](#working-with-arrays)
  - [Arithmetic Functions & Arrays](#arithmetic-functions-arrays)
- [Advanced Formulas](#advanced-formulas)
  - [EACH](#each)
    - [Digital Asset URLs and Metadata](#digital-asset-urls-and-metadata)
    - [Available Metadata Properties](#available-metadata-properties)
    - [System metadata (all are case sensitive):](#system-metadata-all-are-case-sensitive)
    - [Custom Metadata](#custom-metadata)
  - [Mapping to Excel drop-downs / pick lists](#mapping-to-excel-drop-downs-pick-lists)
  - [Using Excel formulas in Templated Exports](#using-excel-formulas-in-templated-exports)
  - [Populating Multiple Sheets and Single-item Sheets with Salsify Excel templates](#populating-multiple-sheets-and-single-item-sheets-with-salsify-excel-templates)

## Working with Variables

Variables are used to store information to be referenced later in a Salsify formula. They provide a way of labeling data with a descriptive name, so formulas can be easier to understand. Using variables can also simplify otherwise very complex formulas. [Click here](https://help.salsify.com/ProductXM/s/article/variables-in-salsify-formulas) to learn more about using variables.

## Working with Arrays

Note in the following syntax examples, {{ }} indicate that you should replace the value with your specific value. Do not include the {{ }} in your final formula.

An array is a list of multiple values in a specific order. Any property in Salsify can have multiple values, and as in the example above you can use the `VALUES` formula to output an array of a property’s values. In addition to the `VALUES` formula there are other ways to generate arrays.

Adding square brackets around values creates an array:

```text
[VALUE("propertyID1"), VALUE("propertyID2"), VALUE("propertyID3")]
```

You can take an array of values and produce a single string (text) value by joining elements of an array with a delimiter as below. Either of these examples will output all values from each property, and insert a new line between values.

```text
JOIN([VALUE("propertyID1"), VALUE("propertyID2"), VALUE("propertyID3")], "")
```
```text
JOIN([VALUE("propertyID1"), VALUE("propertyID2"), VALUE("propertyID3")], "\n")
```

### Arithmetic Functions & Arrays

You can use arrays to apply the same function across multiple values. In this example,

`ADD(2,[3,4,5])` adds 2 to each value and outputs:

- `5.0`
- `6.0`
- `7.0`

See the [Formula Cheat Sheet](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet) for the full list of Salsify formulas.

## Advanced Formulas

### EACH

Use `EACH` to apply functions to arrays of values and simplify formulas. `EACH` eliminates the need to test for existing values with `IF` statements. `EACH` only performs its function where a property value exists.

For example, we want to concatenate a bullet point symbol and space in front of each bullet point. If we used `CONCAT` alone we would get:

_Screenshot: Formula editor showing concatenation of bullet points_

Bullet symbols are inserted, even where we do not have values. We could add an `IF` statement to test for a value, then apply the concatenation like this, but the formula gets more complex:

_Screenshot: Formula builder showing conditional concatenation of bullet points_

`EACH` simplifies this process, and only performs the function where the defined property values exist. The syntax for `EACH` is:

```text
EACH("{{array}}","{{name for single item in array}}" => "{{action you'd like to take}}")
```

So our formula for the above example is:

```text
EACH(VALUES("Bullet Points"), feature => CONCATENATE("• ", feature))
```

and in our result, we only have bullets where we have values for the property.

_Screenshot: Formula builder showing concatenation of bullet points in an array_

You may have cases where adding a number to the bullet can be useful, like adding a label ahead of the value. In that case you can include index in your formula, which will add a number you can use in the result. If we want to add Bullet 1:, Bullet2, etc. to the example we have started, instead of inserting the bullet point character, the formula would be:

```text
EACH(VALUES("Bullet Points"), (feature,index) => CONCATENATE("Bullet",index,":", feature))
```

_Screenshot: Formula builder showing concatenation of bullet points with indexes_

The additional index adds a sequential number to the result. Note that if you include index, wrap it and your other variable in parentheses eg. `(feature,index)`. If you don't use index, don't include the parentheses.

#### Digital Asset URLs and Metadata

You can use `VALUE` to get the URL for any digital assets associated with a product's properties. For example, to get the URL of the 1st product image you would use `VALUE("Product Images", 1)`.

You can get other metadata of a digital asset associated with a product's properties by using `ASSET_VALUE`.

`ASSET_VALUE("{{property name}}", "{{metadata property}}", N)` - Returns the value of the `<metadata_propertyID>` attribute for the Nth digital asset associated with `<propertyID>`. Built-in metadata properties must be prefixed with salsify:. For example, to output the height in pixels of a product's hero image you could use `ASSET_VALUE("Hero Image", "salsify:Height", 1)`.

#### Available Metadata Properties

#### System metadata (all are case sensitive):

- salsify:Id
- salsify:Height
- salsify:Width
- salsify:Name or salsify:Filename
- salsify:Url
- salsify:Source

#### Custom Metadata

To find custom metadata property IDs available in your Salsify account:

1. From the main menu, choose Digital Assets > View All
2. From the Actions menu on the View All Digital Assets, choose Export Metadata. Any that do not begin with salsify: are custom to your organization. You can use these in your formula as well.

`JOIN_ASSET_VALUES("{{property name}}", "{{metadata property}}", "{{delimiter}}")` joins metadata together for all of the digital assets associated with a property. For example, to output the file names of all a product's lifestyle images joined together with commas you could use `JOIN_ASSET_VALUES("Lifestyle Images", "salsify:Filename", ", ")`.

You can learn more about other Salsify formulas for working with digital assets at our [templated Excel exports KB article](https://help.salsify.com/ProductXM/s/article/configuring-product-feedstemplated-exports).

### Mapping to Excel drop-downs / pick lists

Many retailer spreadsheet templates include drop-down lists of acceptable values for a particular column. Often, the values that you have in Salsify are not the same as the values that a retailer requires. In cases where the property is a picklist, see [Value Mapping](https://help.salsify.com/ProductXM/s/article/readiness-report-value-mapping) for a more streamlined way to handle the case. If the property is not a picklist, you can use `LOOKUP` to achieve the same result.

Salsify includes a `LOOKUP` formula (similar to `VLOOKUP` in Excel) that lets you map from your product values in Salsify to the values that the spreadsheet requires. To use `LOOKUP`, follow these steps.

1. Create a two-column lookup table in a new spreadsheet. The first column should be the values that your products have in Salsify, and the second should be the corresponding value that the spreadsheet template asks for. For example, you might setup a lookup table like this to map your product colors to one of your retailer's list of acceptable colors. Your table must contain one row for each Salsify property value, and its corresponding retailer value. You may have duplicate values in the retailer column as shown here:

_Screenshot: Excel spreadsheet with two columns Salsify Color and Retailer Color_

2. Save the spreadsheet and upload the file to Salsify digital assets.
3. View the uploaded file and copy the asset ID, located at the top of the asset details on the left.

_Screenshot: Digital Assets Detail Page with ID highlighted_

4. Use this formula in your Readiness Report or Excel template mapping: `LOOKUP(VALUE("Color"), "{{asset_ID}}", "Retailer Color", "N/A")`. The first argument to `LOOKUP` is the value to be looked up (the key). The second value is the asset ID for the spreadsheet (from step 3 above). The third value is the header of the column that contains the value to be returned. The fourth value is an optional value that will be filled in if the looked up (key) value is not found. If this value isn't provided, the lookup will not return a value.

You can also include more than two columns in your lookup table. For example, you can use a single lookup table to map your color values to the different color values used by Amazon, Walmart, and your other customers. In this case, you would add columns to the right of the Retailer Color column, and refer to the corresponding column in your formula. For example, you could store a table that looks like this:

_Screenshot: Spreadsheet with three columns Color, Amazon color, and Walmart color_

You could use the following formulas to access information from this table:

```text
LOOKUP(VALUE("Color"), "941c14ad00cd40fdfcdd2e62ff6aae78658ce06e", "Amazon color")
```

This formula would return Off-White wherever your product value is Natural.

```text
LOOKUP(VALUE("Color"), "941c14ad00cd40fdfcdd2e62ff6aae78658ce06e", "Walmart Color")
```

This formula would return Beige wherever your product value is Natural.

Note that you can update your lookup table at any time by making changes, then choose the replace option in digital assets to retain the same asset ID, but update the spreadsheet contents.

### Using Excel formulas in Templated Exports

Inside Salsify Excel templates, you can also use any regular Excel formula. To do this, put a # in front of the formula. (Note: Regular Excel formulas are not available in the Salsify Readiness Report interface.)

Wherever possible, however, we encourage you to use Salsify formulas. We're regularly expanding the Salsify formula library. If there's a formula you need, please contact Customer Support.

### Populating Multiple Sheets and Single-item Sheets with Salsify Excel templates

Note: The below tip is only for Salsify Excel templates. The Salsify Readiness Report interface can directly generate multi-tab sheets. Please contact your Salsify Customer Success Manager to learn more.

Salsify formulas can only appear on a single row of a single sheet in a template. Follow these steps if you want to use Salsify values on multiple sheets (tabs) in a generated spreadsheet:

1. Create a new tab (sheet) in this spreadsheet. Put it before the other sheet and call it "Master"
2. In the new tab, make column headers for each Salsify values that you need to use throughout the spreadsheet. Below those column headers, put in the `VALUE` or other Salsify formulas to output the values you need.
3. On the other (main) sheets, you're going to use Excel formulas to refer back to the values from the Master sheet. These formulas will look like this: `=""&Master!A2` That formula copies the value from cell A2 on the Master sheet, if there is a value there. You'll do a similar formula to copy the value from B2 on Master to the right place on the main sheet, for C2, etc.
4. Right-click on the tab and choose "Hide". This ensures that the master sheet does not interfere with the spreadsheet form that you are generating.

Note: You can use this same technique to populate retailer item setup sheets that require one sheet per product, rather than one row per product.
