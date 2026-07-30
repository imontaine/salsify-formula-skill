# Salsify Common Formula Use Cases

Source: Salsify “Common Formula Use Cases — Examples & Explanations”
Source last modified: April 27, 2026
Extracted: July 30, 2026

This guide preserves Salsify’s documented explanations and formulas. Function links point to the companion function reference.

## Quick index

- [Add Custom File Names to Digital Asset URLs](#add-custom-file-names-to-digital-asset-urls)
- [Add Leading Zeros to a Value](#add-leading-zeros-to-a-value)
- [Change Date Formatting](#change-date-formatting)
- [Computed Property - Enable Filtering for Variants](#computed-property-enable-filtering-for-variants)
- [Conditional Formula to Achieve a True/False Result](#conditional-formula-to-achieve-a-true-false-result)
- [Convert Measurement Values to Other Units of Measure](#convert-measurement-values-to-other-units-of-measure)
- [Digital Asset URLs and Metadata](#digital-asset-urls-and-metadata)
- [Escape Special Characters in Formulas](#escape-special-characters-in-formulas)
- [Formula Example: EACH_PAIR](#formula-example-each-pair)
- [Templated Exports: How to populate multiple Excel sheets and single-item sheets](#templated-exports-how-to-populate-multiple-excel-sheets-and-single-item-sheets)
- [Map longest dimension to a specific attribute](#map-longest-dimension-to-a-specific-attribute)
- [Mapping to Excel Dropdowns/pick lists - using LOOKUP](#mapping-to-excel-dropdowns-pick-lists-using-lookup)
- [Readiness Report Value Mapping](#readiness-report-value-mapping)
- [Remove Special Characters & Symbols](#remove-special-characters-symbols)
- [Using JOIN_RELATIONS to return a set of related products](#using-join-relations-to-return-a-set-of-related-products)
- [Replace and Remove Characters with Regular Expressions](#replace-and-remove-characters-with-regular-expressions)
- [Return an array of values](#return-an-array-of-values)
- [Round to a Specific Number of Digits After a Decimal Point](#round-to-a-specific-number-of-digits-after-a-decimal-point)
- [Sending pairs of label and value information with COMPOUND](#sending-pairs-of-label-and-value-information-with-compound)
- [Setting a default value & returning a value from a set of properties with COALESCE](#setting-a-default-value-returning-a-value-from-a-set-of-properties-with-coalesce)
- [How to use Universal Properties with Salsify Formulas](#how-to-use-universal-properties-with-salsify-formulas)
- [Working with Arrays](#working-with-arrays)
- [Working with Collections](#working-with-collections)

## Use cases

## Add Custom File Names to Digital Asset URLs

**Functions used:** [`AND`](salsify-functions.md#and), [`ASSET_VALUE`](salsify-functions.md#asset-value), [`AT`](salsify-functions.md#at), [`COMPACT`](salsify-functions.md#compact), [`IF`](salsify-functions.md#if), [`REPLACE`](salsify-functions.md#replace), [`SPLIT`](salsify-functions.md#split), [`VALUE`](salsify-functions.md#value)

In this article, we’ll discuss how to:

- Add a custom file name to a digital asset URL (shareable link)
- Export digital asset URLs with custom file names in bulk using Salsify formulas

When you generate a shareable link for a digital asset stored in Salsify, by default it will have an encrypted file name:

`https://images.salsify.com/image/upload/s--cW1FFtcY--/ev9k9cqknw9uzdnicuaj.jpg`

When you share digital assets with retailers and other partners, some may require the URL to include identifying information in the file name. For example, an image file name may need to include the product ID, product name, and angle code:

`https://images.salsify.com/images/ev9k9cqknw9uzdnicuaj/00123_cardboard-box_left-angle.jpg`

Let’s break down how to add a custom file name to a single shareable link. [Click here](https://help.salsify.com/ProductXM/s/article/dam-getting-shareable-links-for-digital-assets) to learn how to generate a shareable link for a digital asset.

### Add a Custom File Name to a Digital Asset Shareable Link

1. Remove `image/upload/#######/` from the URL and replace it with `images`.

**Before**: `https://images.salsify.com/image/upload/s--cW1FFtcY--/ev9k9cqknw9uzdnicuaj.jpg`

**After**: `https://images.salsify.com/images/ev9k9cqknw9uzdnicuaj.jpg`

2. Remove the file extension and replace it with a forward slash (/) followed by the new file name and file extension.

**Before**: `https://images.salsify.com/images/ev9k9cqknw9uzdnicuaj.jpg`

**After**: `https://images.salsify.com/images/ev9k9cqknw9uzdnicuaj/00123_cardboard-box_left-angle.jpg`

For raw files like XLSX or CSV, you’ll use the same approach, but substitute `files` for `images`

1. Remove `raw/upload/#######/` from the URL and replace it with `files`

**Before**: `https://images.salsify.com/raw/upload/s--c7x0eXPc--/ds9zfjfzzpq7d4ozvrgy.xlsx`

**After**: `https://images.salsify.com/files/ds9zfjfzzpq7d4ozvrgy.xlsx`

2. Remove the file extension and replace it with a forward slash (/) followed by the new file name and file extension.

**Before**: `https://images.salsify.com/files/ds9zfjfzzpq7d4ozvrgy.xlsx`

**After**: `https://images.salsify.com/files/ds9zfjfzzpq7d4ozvrgy/00123_cardboard-box_data-sheet.xlsx`

Now that we’ve reviewed how to update individual links, let’s look at how to export digital asset URLs with custom file names in bulk.

### Export Digital Asset URLs with Custom File Names using Salsify Formulas

To learn more about the formula functions used in these examples, see the [Formulas Cheat Sheet](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet).

#### Custom File Names from Existing Properties

With this approach, you can generate a file name using a property value or combination of property values stored in Salsify. To use the formula below:

- Replace **Main Image** with the property ID where your digital assets are stored.
- Replace **VALUE("Product Name")** with a formula that will generate your new filename. For example, to generate a filename that combines the SKU and Product Name, you may use: `CONCAT(VALUE(“SKU”),”_”,VALUE(“Product Name”))`

```text
LET imageurl = VALUE("Main Image") IN
LET newname = VALUE("Product Name") IN

IF(
AND(imageurl,newname),
CONCAT(
"https://images.salsify.com/images/",
REPLACE(AT(SPLIT(imageurl,"/"),"7"),".jpg",""),
"/",
newname,
".jpg"
)
)
```

#### Custom File Names from Digital Asset Metadata

If you have custom file names stored as [Digital Asset Metadata](https://help.salsify.com/ProductXM/s/article/dam-getting-started-with-digital-asset-metadata), then this approach will allow you to export digital asset URLs that include the stored file name.

To use this formula, replace the two instances of **Main Image** with the property ID where your image is stored.

```text
LET imageurl = VALUE("Main Image") IN
LET newname = ASSET_VALUE("Main Image","salsify:Name",1) IN

IF(
AND(imageurl,newname),
CONCAT(
"https://images.salsify.com/images/",
REPLACE(AT(SPLIT(imageurl,"/"),"7"),".jpg",""),
"/",
newname
)
)
```

#### Set a Custom File Name and an Image Transformation

With this approach, you can generate a file name using a property value or combination of property values stored in Salsify and add an image transformation. [Click here](https://help.salsify.com/ProductXM/s/article/dam-getting-started-with-digital-asset-transformations) to learn more about image transformations.

To use this formula:

- Replace **Main Image** with the property ID where your image is stored.
- Replace **VALUE("Product Name")** with a formula that will generate your new filename. For example, to generate a filename that combines the SKU and Product Name, you may use: `CONCAT(VALUE(“SKU”),”_”,VALUE(“Product Name”))`
- Replace **c_limit,w_2000,h_20000** with the transformation to be applied to your images.

```text
LET imageurl = VALUE("Main Image") IN
LET newname = VALUE("Product Name") IN
LET transformation = "c_limit,w_2000,h_20000" IN
LET imageid = COMPACT(AT(SPLIT(AT(SPLIT(imageurl ,"/"),7),"."),1)) IN

IF(
AND(imageid,newname),
CONCAT(
"https://images.salsify.com/images/",
transformation,
"/",
imageid,
"/",
newname,
".jpg"
)
)
```

## Add Leading Zeros to a Value

**Functions used:** [`LPAD`](salsify-functions.md#lpad), [`VALUE`](salsify-functions.md#value)

In cases where you have identifiers that have fewer digits than the attribute requires, you can use a formula to add zeros at the beginning of the number until it is the number of digits in length that you specify.

If you’re unsure if all your identifiers are the correct length, it’s best practice to use `LPAD` in your formula. It won’t change any identifiers that meet requirements.

In this example, `LPAD` adds zeros to the left of the value to make it the length we specified, 12.

To use this example:

1. Copy the formula below
2. Paste into the formula box
3. Replace `your-property` in line 2 with the property ID where your value is stored.

```text
let digits = "12" in
let property = "your-property" in

LPAD(VALUE(property),"0",digits)
```

If you want to create a value with a different number of digits, just replace 12 with the number of digits you need.

## Change Date Formatting

**Functions used:** [`IF`](salsify-functions.md#if), [`MID`](salsify-functions.md#mid), [`VALUE`](salsify-functions.md#value)

In readiness reports, when the attribute is Date format, dates must be formatted in the order YYYY-MM-DD with dashes between. When stored as a date property type in Salsify, this will automatically go into the readiness report in the correct format.

But if you store your dates in a property with a string data type which may be in a different format, you can use the following formulas to adjust to the required format.

To use, choose the format that matches your use case. Replace your-date-id with the property ID that stores the date you want to send. The formula will rearrange the digits to the appropriate order and insert dashes between the date parts to meet the requirement.

**Dates stored as mm/dd/yyyy or mm-dd-yyyy**

```text
#Change date format from mm/dd/yyyy to YYYY-MM-DD
let date = VALUE("your-date-id") in #replace your-date-id with property id
let mm = LEFT(date,2) in
let dd = MID(date,4,2) in
let yyyy = RIGHT(date,4) in

IF(date,CONCAT(yyyy,"-",mm,"-",dd),null)
```

**Dates stored as dd/mm/yyyy or dd-mm-yyyy**

```text
#Change date format from dd/mm/yyyy or dd-mm-yyyy to yyyy-mm-dd
let date = VALUE("your-date-id") in
let dd = LEFT(date,2) in
let mm = MID(date,4,2) in
let yyyy = RIGHT(date,4) in

IF(date,CONCAT(yyyy,"-",mm,"-",dd),null)
```

**Dates stored as yyyy/dd/mm or yyyy-dd-mm**

```text
#Change date format from yyyy/dd/mm or yyyy-dd-mm to yyyy-mm-dd
let date = VALUE("your-date-id") in
let mm = RIGHT(date,2) in
let dd = MID(date,6,2) in
let yyyy = LEFT(date,4) in

IF(date,CONCAT(yyyy,"-",mm,"-",dd),null)
```

## Computed Property - Enable Filtering for Variants

**Functions used:** [`PARENT_ID`](salsify-functions.md#parent-id)

This article refers to the parent/variant feature which is not enabled by default for all organizations. If it's not enabled for your organization, [click here](https://help.salsify.com/ProductXM/s/article/variants-and-inheritance) to learn more about parents and variants or reach out to your Customer Success Manager or customer support to discuss having the feature enabled.

There may be cases where you need to be able to filter for just sellable products with or without a parent/variant relationship. With default behavior in Salsify, you can choose whether or not to view base or sellable products, but products without a parent/variant relationship appear in both sets of filter results.

To filter for just variant products, or just solo products, you can add a computed property that places the parent ID in all the variant products. Then to return only variant products, from the sellable products view, you can filter for just the products that have a value in the field. To see only solo products, filter from the sellable products view for only products that do not have a value in the field.

To set up the computed property:

1. From the More menu, choose Properties.
2. In the *Actions* menu, choose *New Property*.
3. Name your property something you'll recognize (eg. Parent ID) and check the Computed Property checkbox.
4. Click *Create*.
5. In the formula box, use the formula `PARENT_ID()`
6. Click Save.

When the computed property updates through all your products you'll be able to filter by the new property. Only variants will have a parent ID value in the property, and you can filter by your new property.

## Conditional Formula to Achieve a True/False Result

**Functions used:** [`EQUAL`](salsify-functions.md#equal), [`IF`](salsify-functions.md#if), [`VALUE`](salsify-functions.md#value)

In cases where you need a true/false answer, you can use a conditional formula to test for an existing value, and return a Boolean result (true/false, Y/N). Note that in readiness reports, the report is typically set up to return the version of the Boolean true/false answer in the format that the endpoint requires. So you only need to set up the formula to return the correct T/F result and the readiness report will take care of the proper syntax.

The `IF` function can test for a true/false based on a property value. For example, you may have a case where you need to fill in a true/false about whether a product contains or requires batteries, but you don't store the T/F value. Your product does contain a battery type field, and it's blank if it doesn't contain or take batteries. You can use an `IF` formula to produce the true/false answer.

### Test for Any Value

This formula checks for the existence of a value in the property Battery Type, and if any value is present, it returns T, and if not it returns F.

To use this formula, replace `Battery Type` with your property ID.

```text
IF(VALUE("Battery Type"),"T","F")
```

### Test for a Specific Value

Use `EQUAL` to check a property's value and return an answer based on what the formula finds. In the example, we need know whether or not the product takes a lithium battery, and we have an enumerated property called Battery Type that lists all the battery options.

This formula is recommended for use with enumerated properties to avoid differences because of other spellings, though you can also solve for that by checking for a list of possible options.

In the example, we're testing for a specific battery type by adding the EQUAL function. It tests for the existence of a value stored in the property that matches the value we specify in the formula, and returns true or false based on whether the values match. Note that the formula is case sensitive, so in the formula below, the value `lithum` or `LITHIUM` would return a false result.

To use this formula, replace `Battery Type` with your property ID, and `Lithium` with the value you want to test for.

```text
EQUAL(VALUE("Battery Type","Lithium")
```

## Convert Measurement Values to Other Units of Measure

**Functions used:** [`MULTIPLY`](salsify-functions.md#multiply), [`VALUE`](salsify-functions.md#value)

In these formulas, we're applying math to one unit of measure and converting it to another. We can do the formula one of two ways - with or without variables. It's completely up to your preference which version you choose.

We'll show you the formula for both, and then break down how each works.
**Pro Tip**: Not sure what conversion math you need to get from one unit to the other? Google knows. Just enter the unit you have and the unit you need (like inches to cm) and a conversion tool will appear.

[Click here](#measurement-non-variable) to jump to Measurement Conversion using a Non-variable Formula

#### Measurement Conversion using Variables

In this method, we're using variables to hold the details of the conversion so that it's simple to update to other cases. In our example, we have inches stored in our property, and we need it converted to centimeters. We can use this formula to store a value in Salsify using computed properties, or we can apply the formula in a readiness report or templated export if it's not something we need available to multiple endpoints or in a catalog. [Click here](https://help.salsify.com/ProductXM/s/article/in-app-computed-properties) to learn more about computed properties.

We're using variables in this case because we know we have other dimensions to convert, and this is a simple way to make updates without changing the formula itself, and to make the formula more understandable to other team members who may need to work with it.
*Note: Variables are currently supported in Readiness Report and computed property formulas, but not available in templated exports.*

```text
#Convert inches to cm
let original = VALUE("Product Length") in
let conversion = "2.54" in

MULTIPLY(original,conversion)

```

Here's a line by line breakdown of our formula (text below, video above)

1. `#Convert inches to cm` The `#` here indicates this is a comment, and nothing after it will be calculated. It can be used at the beginning of a line or after a formula, and it's a way to add explanation for more complicated formulas. In this case, we're using it to just explain what this formula does. We could also use it after a specific line to describe what that line does.
2. `let original = VALUE("Product Length") in` This is a variable statement. In logical terms, this line is saying let the term we chose, `original` (it could be any term without spaces, and it's case sensitive) be a variable that holds the value of what's after the `=` sign. Now anywhere `original` shows up in the formula, it will insert the value for `Product Length`. We happen to just be storing a value here, but we could also make the variable store the result of a formula calculation. `in` ends the line to tell Salsify where to stop.
3. `let conversion = "2.54" in` This variable `conversion` stores the value we'll use to multiply our `Product Length` by. Storing this in a variable makes it easy to reuse this formula for other conversions like ounces to grams. By just changing the number, the formula will recalculate based on it without making changes in the formula itself.
4. We inserted a blank line here just for clarity to split the variables section from the final formula. When using the formula editor, you can use blank lines and indentations wherever they're helpful.
5. `MULTIPLY(original,conversion)`The formula itself. Now we're using the variables we defined, and writing a simple formula that multiplies our `original` value by the `conversion` value and returns the metric equivalent to our inches value. So with this formula if our product length is 1 inch, the value returned by the formula will be 2.54 centimeters. In our example below, the product length for the first bag listed was 20 inches, and the preview shows 50.8 cm, so we know we've done the formula correctly.

#### Measurement Conversion Using a Non-Variable Formula

Here's another option to write the same formula without variables. The same formula from above would look like this:

```text
#Convert Product Length inches to cm
MULTIPLY(VALUE("Product Length"),"2.54")

```

In this example, this version is more compact without variables, and may be easier for you to manage. Again, either method is valid, and there are circumstances where one or the other is an easier choice. Use whatever works best for you.

In this case, we still have the comment line at the beginning explaining what the formula does, and our formula is all one one line now without the variable stand ins. The `MULTIPLY` formula uses the value from our product length property directly, and multiplies it by the value 2.54 to get the same results:

## Digital Asset URLs and Metadata

**Functions used:** [`ASSET_VALUE`](salsify-functions.md#asset-value), [`JOIN`](salsify-functions.md#join), [`JOIN_ASSET_VALUES`](salsify-functions.md#join-asset-values), [`SUBSTITUTE`](salsify-functions.md#substitute), [`TRANSFORM_ASSET_URL`](salsify-functions.md#transform-asset-url), [`VALUE`](salsify-functions.md#value), [`VALUES`](salsify-functions.md#values)

You can use `VALUE` to get the URL for any digital assets associated with a product's properties. For example, to get the URL of the 1st product image you would use `VALUE("Product Images", 1)`.

You can get other metadata of a digital asset associated with a product's properties by using `ASSET_VALUE`.

`ASSET_VALUE("<property name>", "<metadata property>", N)` - Returns the value of the <metadata_propertyID> attribute for the Nth digital asset associated with <propertyID>. Built-in metadata properties must be prefixed with salsify:. For example, to output the height in pixels of a product's hero image you could use `ASSET_VALUE("Hero Image", "salsify:Height", 1)`.

### Available Metadata Properties

#### System metadata (all are case sensitive):

*Prefix name of each with salsify: in formulas. Metadata property IDs are case sensitive.*

**All file types**

- Source url
- Etag
- Bytes
- Width
- Format
- Height
- Filename
- Resource type
- Name
- Id

**Video Metadata Properties**

- Video id
- Provider
- Title
- Description
- Duration
- Date
- Embed url
- Embed code

**PDF Metadata Properties**

- Pages

#### Custom Metadata

To find custom metadata property IDs available in your Salsify account:

1. From the main menu, choose *Digital Assets > View All*
2. From the Actions menu on the *View All Digital Assets*, choose *Export Metadata*. Any that do not begin with `salsify:` are custom to your organization. You can use these in your formula as well.

`JOIN_ASSET_VALUES("<property name", "<metadata property>", "<delimiter>") `Joins metadata together for all of the digital assets associated with a property. For example, to output the file names of all a product's lifestyle images joined together with commas you could use `JOIN_ASSET_VALUES("Lifestyle Images", "salsify:Filename", ", ")`.

You can learn more about other Salsify formulas for working with digital assets at our [templated Excel exports KB article](https://help.salsify.com/ProductXM/s/article/configuring-product-feedstemplated-exports).

### Image URL Transformation

Use the `TRANSFORM_ASSET_URL` formula to create image URL transformations, most commonly used in channels to send images in a specific format for dedicated endpoints or custom feed exports.

[Click here](https://help.salsify.com/ProductXM/s/article/image-transformations-cheat-sheet2) for a list of available image transformations.

With `TRANSFORM_ASSET_URL`, you choose the property to pull digital assets from, specify the transformation to apply to the URL and choose the property value position to pull the asset from.

The syntax for this formula is: `TRANSFORM_ASSET_URL("<propertyID>", "<transformation_string>","<optional_index>")` where `<propertyID>` is the property you want to pull the value from, `<transformation_string>` is the transformation to apply to the digital asset, and `<optional_index>` specifies which digital asset to pull from the property. Index is optional, and if not specified, the formula will use the first digital asset in the property.

For example:

`TRANSFORM_ASSET_URL("Additional Product Images", "c_fit,w_200,h_200",2)`

In this example, *Additional Product Images* is the property ID, and `c_fit,w_200,h_200` is the image transformation. The index is 2, so the second property value will be delivered. The image is transformed with the instructions:

- `c_fit`: retain the original proportions and fit within the dimensions of
- `w_200`: 200 pixels wide
- `h_200`: 200 tall

Original: [https://images.salsify.com/image/upload/s--RIotHb57--/ixndvaite1irreeimtsm.jpg](https://images.salsify.com/image/upload/s--RIotHb57--/ixndvaite1irreeimtsm.jpg)

Transformed: [https://images.salsify.com/image/upload/s--RIotHb57--/c_fit,w_200,h_200/ixndvaite1irreeimtsm.jpg](https://images.salsify.com/image/upload/s--RIotHb57--/c_fit,w_200,h_200/ixndvaite1irreeimtsm.jpg)

#### Deliver multiple transformed image URLs

Combine `TRANSFORM_ASSET_URL` with other functions to create formulas that deliver multiple images. To build on the example above, combine multiple transformations with JOIN to deliver a set of images to an endpoint. Each image can contain a different transformation, and you can pull from multiple properties.

In this example, 5 images are sent to the endpoint. The first image is the first value in the *Main Image* property, and the other 4 images sent are from the *Additional Product Images* property. The formula can be written in two ways with the same result. To use these examples, replace the property name (`Main Image`, `Additional Product Images`), and transformation you want to make (`c_fit,w_200,h_200`).

##### Variable Example

In this example, the formula defines 5 variables, (*image1 - image5*) and each holds a separate transformed value. The final formula uses `JOIN` to combine the values and insert a line break between each.

```text
let image1= TRANSFORM_ASSET_URL("Main Image","c_fit,w_200,h_200") in

let image2= TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200") in

let image3 = TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",2) in

let image4 = TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",3) in

let image5 = TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",4) in

JOIN([image1,image2,image3,image4,image5],"\n")
```

##### Non-Variable Example

In this example, the formula contains an array of calculations. Each line inside the array (the lines enclosed in brackets [ ]) defines an image to apply a transformation to, and JOIN combines them, separating them with a line break.

```text
JOIN(

[

TRANSFORM_ASSET_URL("Main Image","c_fit,w_200,h_200"),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200"),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",2),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",3),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",4)

],

"\n"

)
```

#### Transform Image Format

The following formula uses variables to store the format you want to convert the images to (`new_format`), and the image URLs (`image`). Then the formula itself evaluates each URL and when it finds one of the extensions listed, it substitutes the new format extension.

To adjust the formula, replace `".jpg"`; in the `new_format` variable definition to the extension you want to update to, and substitute your property name for `Additional Product Images`.

##### Variable Example

```text
let new_format = ".jpg" in

let image = VALUES("Additional Product Images") in

SUBSTITUTE(

image,

".gif",new_format,

".png",new_format,

".bmp",new_format,

".svg",new_format,

".tiff",new_format,

".tif",new_format,

".eps",new_format

)
```

##### Non-Variable Example

```text
SUBSTITUTE(

VALUES("Additional Product Images"),

".gif",".jpg",

".png",".jpg",

".bmp",".jpg",

".svg",".jpg",

".tiff",".jpg",

".tif",".jpg",

".eps",".jpg"

)
```

#### Transform Image Format and Apply Transformation

Combine the methods above to transform images and deliver them in a specific format. Variables make this more complex formula easier to write and understand.

In this example, we first set variables to hold the image transformations. The transformed variable stores the result of the `JOIN` from the Deliver Multiple Transformed URLs example above. Finally we apply the substitution from the transform image format example above, which will deliver the transformed URLs in jpg format. Change the variable values to use this formula to tailor to your use case.

##### Variable Example

```text
#apply image transformations

let image1= TRANSFORM_ASSET_URL("Main Image","c_fit,w_200,h_200") in

let image2= TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200") in

let image3 = TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",2) in

let image4 = TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",3) in

let image5 = TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",4) in

#store transformations in a variable

let transformed = JOIN([image1,image2,image3,image4,image5],"\n") in

#define the new image format

let new_format = ".jpg" in

#update transformed URLs to the new format

SUBSTITUTE(

transformed,

".gif",new_format,

".png",new_format,

".bmp",new_format,

".svg",new_format,

".tiff",new_format,

".tif",new_format,

".eps",new_format

)
```

##### Non-Variable Example

This example achieves the same results as the variable example above.

```text
SUBSTITUTE(

JOIN(

[

TRANSFORM_ASSET_URL("Main Image","c_fit,w_200,h_200"),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200"),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",2),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",3),

TRANSFORM_ASSET_URL("Additional Product Images","c_fit,w_200,h_200",4)

],

"\n"

),

".gif",".jpg",

".png",".jpg",

".bmp",".jpg",

".svg",".jpg",

".tiff",".jpg",

".tif",".jpg",

".eps",".jpg"

)
```

## Escape Special Characters in Formulas

**Functions used:** [`SUBSTITUTE`](salsify-functions.md#substitute), [`VALUE`](salsify-functions.md#value)

There are cases where you will need to use special characters as values in formulas. In these cases, you need to indicate that the formula shouldn't use the character to evaluate what's next but treat it as a value. For example, you may want to concatenate quotation marks in a value or build a formula to remove special characters from values. In these cases, you will escape the special character to indicate that the formula should add it to your string.

Note that Salsify will handle special characters found in your values. So if you are storing values containing special characters, they will appear correctly on their own. Check the readiness report help text for any endpoint requirements regarding special characters.

### Characters to Escape in Formulas

- **`'` single-quote** - This only needs to be escaped if single quotes are used elsewhere in the formula. You can avoid the need to escape single quotes by using double quotes in your formula.
- **`"` double quote - **Like single quotes, only need to be escaped if double quotes are used in your formula. Avoid the need to escape by using single quotes in your formula.
- **`“ ”` curly quotes (single or double)** - Escape in all cases, but can be wrapped in single or double quotes, or escaped with a backslash.
- **`\` backslash - Back slash** can only be escaped with the forward slash method. As with other values, wrap in quotes `"\\"`.
- `\n`** new line** - Used in cases where you need to split a value into two separate values. Use `"\n"` to insert a new line.

### How to Escape Characters

There are three methods to escape characters.

- **Backslash before the character to be escaped** - This is the most consistently reliable method. Add a backslash `\` before the character to be escaped. The formula editor will highlight the backslash and the escaped character in orange. Works in all escape cases. See the example below for usage.
- **Wrap character in single or double quotes** - You can escape a character by wrapping it in the type of quote you are not using in the formula. So for example, if you need to use a single quote as a value in your formula, use double quotes in the rest of the formula and wrap the single quote in double quotes.

#### Formula Example

In this example, we have a property value where the copy writer got a bit carried away with punctuation. So we need to clean it up. We also need our final value to be in the format `product ID / eCommerce Description`. Here's the stored value for *eCommerce Description*:

We want to remove the double quotes, single quotes and curly quotes in this example. So we'll need to substitute those out. And we need to concatenate the two values with a slash between. To make this formula as readable and efficient as we can, we'll use a variable to store our `SUBSTITUTE` process, then perform the concatenate in the final formula.

##### Step 1: Test the formula to remove the quotation marks

We'll use `SUBSTITUTE`, with four lines and we'll use the backslash method to escape our various quotation marks. Before we set the variable, we can test the `SUBSTITUTE` formula to be sure we have the right syntax, and the preview gives us the result we're looking for:

```text
SUBSTITUTE(
VALUE("eCommerce Description"),
"\"","",
"\'","",
"\“","",
"\”",""
)
```

In this case, we're pulling the value from the eCommerce Description property and in each line of the formula, `SUBSTITUTE` is instructed to find the first value, and replace it with the second. So in the first line, we're replacing " with a blank value. We used the backslash to escape the value we were looking for " and wrapped it, and the value we replaced it with, no value, within double quotation marks.

The previewed result at the bottom shows all our stray punctuation has been removed, so next we'll set it up in a variable to make the final formula easy to read and update.
**Pro Tip:** Use Autocomplete to easily pull up the correct property ID and its syntax. Start typing the name of the property, then hold down the ctrl key and spacebar, then pick your property from the drop-down menu.

##### Step 2: Set the description variable

Now that we know the syntax is correct, we'll wrap that in the variable we want to use in our final formula.

```text
let description = SUBSTITUTE(VALUE("eCommerce Description"),
"\"","",
"\'","",
"\“","",
"\”","")
in
```

Next, we could either store our Product ID in another variable or use it directly in the final formula. Since the formula is still very readable and easy to update without adding another variable, we'll just the *Product ID* property directly in the final formula.

##### Step 3: Add the final formula - chain the values, escape the backslash

Finally, we'll use the description variable in our `CONCAT` formula and chain the elements we need to deliver. We add a backslash in front of the backslash to add the character to the final value.

```text
let description = SUBSTITUTE(VALUE("eCommerce Description"),
"\"","",
"\'","",
"\“","",
"\”","")
in

CONCAT(VALUE("Product ID")," \\ ",description)
```

The preview shows the result we're looking for, so we'll save the final formula.

## Formula Example: EACH_PAIR

**Functions used:** [`COLLECTION`](salsify-functions.md#collection), [`EACH`](salsify-functions.md#each), [`EACH_PAIR`](salsify-functions.md#each-pair), [`EQUAL`](salsify-functions.md#equal), [`IF`](salsify-functions.md#if)

The EACH_PAIR function is only available to Advance customers.

Use EACH_PAIR to apply functions to collections of key-value pairs and traverse complex structured data. EACH_PAIR returns an array whose elements are the results of the provided function applied to each key-value pair in a collection. EACH_PAIR compacts the resulting array, filtering out any null values.

For example, we want to serialize each key-value pair as a string:

```text
LET col = COLLECTION('color', 'blue', 'material', 'cotton') IN
EACH_PAIR(col, (key, value) => CONCAT(key, ' is ', value))

#output => ['color is blue', 'material is cotton']

```

EACH_PAIR applies the CONCAT function to each key-value pair of the provided collection, generating a string that joins each key and value with ‘ is ‘.

When the provided function returns null, that result is omitted from the array returned by EACH_PAIR:

```text
LET col = COLLECTION('color', 'blue', 'material', 'cotton') IN
EACH_PAIR(col, (key, value) => IF(
EQUAL(key, 'color'),
CONCAT(key, ' is ', value)
))

#output => ['color is blue']

```

EACH_PAIR can be used to transform collections into other collections:

```text
LET col = COLLECTION('color', 'blue', 'material', 'cotton') IN
EACH_PAIR(col, (key, value) => COLLECTION(
'key', key,
'value', value
))

#output => [{ "key": "color", "value": "blue" }, { "key": "material", "value": "cotton" }]
```

EACH_PAIR can be combined with EACH and itself for transforming nested arrays and collections:

```text
LET col = COLLECTION(
'shirt', COLLECTION('large', ['blue'], 'medium', ['blue', 'green']),
'pants', COLLECTION('small', ['blue', 'green'], 'medium', ['green'])
) IN

EACH_PAIR(col, (clothing, sizes) => EACH_PAIR(
sizes,
(size, colors) => EACH(
colors,
(color) => CONCAT(size, ' ', color, ' ', clothing)
)))

#output => ['large blue shirt', 'medium blue shirt', 'medium green shirt', 'small blue pants..]
```

## Templated Exports: How to populate multiple Excel sheets and single-item sheets

**Applies to**: [Configuring Templated Exports](https://help.salsify.com/ProductXM/s/article/configuring-product-feedstemplated-exports)

To learn more about using formulas in a Custom Channel Templated Export, see:

- [https://help.salsify.com/ProductXM/s/article/configuring-product-feedstemplated-exports#preparing-a-template](https://help.salsify.com/ProductXM/s/article/configuring-product-feedstemplated-exports#preparing-a-template)
- [https://help.salsify.com/ProductXM/s/article/A-Technical-Guide-to-Converting-Formulas-for-Templated-Export-Use](https://help.salsify.com/ProductXM/s/article/A-Technical-Guide-to-Converting-Formulas-for-Templated-Export-Use)

#### Using Excel formulas in Templated Exports

Inside Salsify Excel templates, you can also use any regular Excel formula. (Note: Regular Excel formulas are not available in the Salsify Readiness Report interface.)

#### Populating Multiple Sheets and Single-item Sheets with Salsify Excel templates

Note: The below tip is only for Salsify Excel templates. The Salsify Readiness Report interface can directly generate multi-tab sheets. Please contact your Salsify Customer Success Manager to learn more.

Salsify formulas can only appear on a single row of a single sheet in a template. Follow these steps if you want to use Salsify values on multiple sheets (tabs) in a generated spreadsheet:

1. Create a new tab (sheet) in this spreadsheet. Put it before the other sheet and call it "Master"
2. In the new tab, make column headers for each Salsify values that you need to use throughout the spreadsheet. Below those column headers, put in the `VALUE` or other Salsify formulas to output the values you need.
3. On the other (main) sheets, you're going to use Excel formulas to refer back to the values from the Master sheet. These formulas will look like this: `=""&Master!A2 `That formula copies the value from cell A2 on the Master sheet, if there is a value there. You'll do a similar formula to copy the value from B2 on Master to the right place on the main sheet, for C2, etc.
4. Right-click on the tab and choose "Hide". This ensures that the master sheet does not interfere with the spreadsheet form that you are generating.
Note: You can use this same technique to populate retailer item setup sheets that require one sheet per product, rather than one row per product.

Certain retailers have single-item setup sheets, sell sheets and other non-standard templates that are not accepted for standard Readiness Reports. These retailer templates can be set up to manually create accepted templated exports by following the steps below.

1. Create a new tab (sheet) in the retailer template spreadsheet. Put it before the retailer template sheet and call it "Master". The export will populate this tab.
2. In the new tab, transpose the column headers for each value that you need to use from the original retailer template.
3. Below those column headers, map the attribute with the Salsify formula or hardcoded VALUE and insert a cell reference for the 'master' sheet in the cell that needs to be populated. You will do a similar formula to copy the value from B2 on Master to the right place on the main sheet, for C2, etc.
4. Once all of the attributes are mapped, create a new custom channel using this template as the templated export and publish to the channel one product at a time.

[Click here](https://help.salsify.com/ProductXM/s/article/configuring-product-feedstemplated-exports) to learn more about configuring templated exports.

These templates are common for Sam's Club, Costco, BJ's, CVS, and others. Repeat this process for these templates, adding each sheet’s headers to the master sheet and adding formulas that fill in the subsequent sheets.

## Map longest dimension to a specific attribute

**Functions used:** [`IF`](salsify-functions.md#if), [`MAX`](salsify-functions.md#max), [`MEDIAN`](salsify-functions.md#median), [`MIN`](salsify-functions.md#min), [`REPLACE`](salsify-functions.md#replace), [`ROUND`](salsify-functions.md#round), [`VALUE`](salsify-functions.md#value)

In some cases, you may need to map the your package dimensions to specific attributes based on which is longest to shortest. For example, Walmart Supplier Center requires that the longest product dimension always be mapped to “depth”. However, you may have products that have their longest dimension stored in width or height and it may vary between products. You may also have units of measure stored with your values that don't match the endpoint's requirement. And finally, often you need to round your values to a specific number of digits.

In these cases, you can use variations of this formula to map all three dimension attributes. This formula will:

- Remove any non-numeric characters stored with your number values
- Round the number to the digits you specify, or you can choose not to round
- Return the length you specify - longest, medium or shortest
- Append the UOM you specify to meet the endpoint requirement, or you can choose to return only a number

To use the formula:

1. Copy the formula from the box below and paste it into the attribute's formula box.
2. Make the adjustments that suit your use case in the first 5 lines:

1. Replace `your-height-property` with the property ID that stores product height.
2. Replace `your-length-property` with the property ID that stores product length.
3. Replace `your-width-property` with the property ID that stores product width.
4. If needed, change digits ="2" to the number of digits you want to round to. If you don't want to round, replace `"2"` with `null`.
5. If needed, change uom = "in" from in to the unit you want to append. To not include a UOM, replace `"in"` with `null`.

3. Uncomment one of the last three lines to match the attribute's requirement

```text
#review and replace
let height = "height-property-id" in #replace height-property-id with your property ID
let width = "width-property-id" in #replace width-property-id with your property ID
let length = "length-property-id" in #replace length-property-id with your property ID
let digits = "2" in #change "2" to null to not round
let uom = "in" in #change "in" to null to not append UOM

#no action needed - scroll to next section
let height = REPLACE(VALUE(height), "[^0-9.]", "") in
let width = REPLACE(VALUE(width), "[^0-9.]", "") in
let length = REPLACE(VALUE(length), "[^0-9.]", "") in
let max = IF(digits,ROUND(MAX(height,width,length),digits),MAX(height,width,length)) in
let median = IF(digits,ROUND(MEDIAN(height,width,length),digits),MEDIAN(height,width,length)) in
let min = IF(digits,ROUND(MIN(height,width,length),digits),MIN(height,width,length)) in

#uncomment only one line: max = longest measure, median = medium, min = shortest
#IF(max,CONCAT(max," ",uom))
#IF(median,CONCAT(median," ",uom))
#IF(min,CONCAT(min," ",uom))

```

## Mapping to Excel Dropdowns/pick lists - using LOOKUP

**Functions used:** [`LOOKUP`](salsify-functions.md#lookup), [`VALUE`](salsify-functions.md#value)

Many retailer spreadsheet templates include drop-down lists of acceptable values for a particular column. Often, the values that you have in Salsify are not the same as the values that a retailer requires. In cases where the property is a picklist, see [Value Mapping](https://help.salsify.com/ProductXM/s/article/readiness-report-value-mapping) for a more streamlined way to handle the case. If the attribute in the readiness report is not a picklist, you can use `LOOKUP` to achieve the same result.

Salsify includes a `LOOKUP` formula (similar to `VLOOKUP` in Excel) that lets you map from your product values in Salsify to the values that the spreadsheet requires. There are a couple things to keep in mind when using `LOOKUP`:

- While it's not required, it's best practice to use `LOOKUP` with picklist data type properties.
- If a new value is added to the picklist in Salsify, you'll need to update the Excel `LOOKUP` table to include the new value and corresponding endpoint values.
- If a value associated with a product is not listed in the lookup table, or doesn't have a corresponding endpoint value, the formula will return the default value. If a default isn't specified, the product will not successfully validate and if the attribute you're mapping is required, it won't be sent to the endpoint until the error is corrected.
- Each value you include in column A has to have a corresponding value in the endpoint column in order to validate successfully, unless you provide a default value. The default value will be returned in any case where a product has a value that doesn't match anything in the table, or has no value.
- You can use the same endpoint value for multiple matching Salsify values.
- When using a picklist property data type, always use the ID, not the name, in your lookup table.

To use `LOOKUP`, follow these steps.

1. Create a two-column lookup table in a new spreadsheet. Each column should have a title in row 1, then each row below should contain a unique product value in column A and its corresponding endpoint value in subsequent column(s). All Salsify product values should be included in the table.

- The first column should be the values stored with your products in Salsify.

- If you're using a picklist property, [click here](https://help.salsify.com/ProductXM/s/article/download-organization-data) for help downloading the list of values. Use the property values data type, and copy the IDs for the property values in the Salsify property you want to use.
- If you're using another property data type, export the property for all products to an Excel spreadsheet, copy the property values, then remove duplicates and use the results as your values in column A.
- If your picklist is hierarchical, use the lowest level of the hierarchy as your value. For example, if your hierarchy is *Luggage > Wheeled Luggage*, use *Wheeled Luggage* as the value in the table.

- The second column should be the corresponding value that the spreadsheet template asks for. For example, you might setup a lookup table like this to map your product colors to one of your retailer's list of acceptable colors. Your table must contain one row for each Salsify property value, and its corresponding retailer value. You may have duplicate values in the retailer column as shown here:

2. Save the spreadsheet and upload the file to Salsify digital assets or SFTP location. [Click here](https://help.salsify.com/ProductXM/s/article/dam-getting-started-with-digital-assets) for help uploading digital assets. When using SFTP, replace the asset ID in the example below with the URL of the asset location.
3. View the uploaded file and copy the asset ID, located at the top of the asset details on the left.

4. Use a `LOOKUP` formula in your readiness report or Excel template mapping. Remember to prefix the functions with `SALSIFY_` if you're working with a templated export. For the example above, the formula would be:
`LOOKUP(VALUE("Color"), "941d14ad99cd49fdfcdd2e62ff6aae7858ce06e", "Retailer Color", "N/A")`

or in a templated export:
`SALSIFY_LOOKUP(SALSIFY_VALUE("Color"), "941d14ad99cd49fdfcdd2e62ff6aae7858ce06e", "Retailer Color", "N/A")`

In this case, the formula:

- retrieves the value stored in the Color property for the product
- looks in the Excel spreadsheet stored in the Salsify asset ID `941d14ad99cd49fdfcdd2e62ff6aae7858ce06e`
- finds the value in column A, the color stored in Salsify
- returns the value in in column B, the Retailer Color
- if there's no value, it returns `N/A`. Default value is optional, so you can specify whatever default text you want in place of `N/A`, or remove that from the formula.

So from the example above, if the product had `Aqua` stored as the color value, the value returned by the readiness report or templated export would be `Aqua`. If the product had a value of `Green` which isn't listed in the table, the formula would return `N/A`.

You can use the same lookup table to return results for multiple target schemas. The value stored in Salsify remains in the first column, but you can add additional columns for other retailers. So in this example, the corresponding Amazon colors are in column B, and Walmart colors in column C. In this case, you would add columns to the right of the Retailer Color column, and refer to the corresponding column in your formula.

You could use the following formulas to access information from this table:
`LOOKUP(VALUE("Color"), "941c14ad00cd40fdfcdd2e62ff6aae78658ce06e", "Amazon color")`
This formula would return Off-White wherever your product value is Natural.

`LOOKUP(VALUE("Color"), "941c14ad00cd40fdfcdd2e62ff6aae78658ce06e", "Walmart Color")`
This formula would return Beige wherever your product value is Natural.

Note that you can update your lookup table at any time. To make changes, download the table from digital assets, update and save your changes, then choose the replace option in digital assets to upload the new table.

## Readiness Report Value Mapping

Use Value Mapping when a retailer requires a specific set of picklist values, and you have a property that contains values that are similar but not exactly what the retailer is asking for. Value Mapping makes associations between your property values and the retailer’s, so that you can send exactly what the retailer requires.

Think of Value Mapping as a way to say, “if I'm using THIS value in Salsify, I want to send THAT value to the retailer.”

Typically, Value Mapping is used to match the product categories that you store in Salsify to those defined by a retailer.

### Value Mapping Setup

1. Click the pencil icon next to the attribute that you want to map.
2. Click *No Entry.*

3. At the top of the *Edit Mapping Source* page, you can view key attribute details, such as its data type and whether it is required or optional. For further guidance, you can expand the section to view our specific mapping recommendations.

4. Between *Choose Source* options, select *Value mapping*.
5. Choose the property you want to map to.
6. Click *Download starter template*.

7. For each of your properties on the first tab, choose a corresponding retailer property ID from the second tab, and paste it into column C on the first tab.
When completed, you’ll have one retailer value for each of your property’s values.

**Important note:** Each row in column C must be filled in, or the mapping will produce errors in the readiness report.
8. Save the spreadsheet and upload to Salsify.

9. Click *Save*.
10. Click *Refresh* to see the new percentage of completion for your attribute. If it’s not at 100%, review the products to make sure that they have values stored in the property that you selected, or use [Retailer Edits](https://help.salsify.com/ProductXM/s/article/getting-started-with-retailer-edits) to complete the requirements. Please note that retailer edits overwrite mapped values.

#### Example Scenario

Your products come in 12 different colors: `Ruby, Scarlet, Crimson, Gold, Daisy, Sunlight, Chartreuse, Pistachio, Emerald, Sapphire, Cobalt, and Navy`. These colors are managed in Salsify under a picklist property.

The retailer that you need to submit your products to only accepts four specific colors: `Red, Yellow, Green, and Blue`

Readiness Report Value Mapping will allow you to say **“if I'm using THIS color on Salsify, I want to send THAT color to the retailer.”**

Start by downloading the Value Mapping template. The first tab shows the 12 Color values stored in Salsify and the second tab sheet shows the four values from the retailer.

Pick which retailer values are the best match for your values. The retailer's first option is "Red." This fits for Ruby, Scarlet, and Crimson, so you'd copy the retailer's "Red" from the second sheet and paste it into column C for Ruby, Scarlet, and Crimson. Likewise, Gold, Daisy, Sunlight can be mapped as "Yellow”; Chartreuse, Pistachio, Emerald can be mapped as "Green"; and Sapphire, Cobalt, and Navy can be mapped as "Blue".

After all 12 of your values are mapped to the specific retailer-accepted values, just save and upload the template to the Readiness Report and refresh the channel.

#### Alternative Approaches

If the property values that you store in Salsify are not a good match for the retailer, you could either create an enumerated/picklist property and use the retailers values as the values or use [Retailer Edits](https://help.salsify.com/ProductXM/s/article/getting-started-with-retailer-edits) to enter values directly in the Readiness Report.

## Remove Special Characters & Symbols

**Functions used:** [`CLEAN_TEXT`](salsify-functions.md#clean-text), [`SUBSTITUTE`](salsify-functions.md#substitute), [`VALUE`](salsify-functions.md#value)

Some retailers allow you to use only alphanumeric characters. Use CLEAN_TEXT to remove all non-alphanumeric characters, and SUBSTITUTE to remove only specific symbols or characters.

For instance, if you would like to remove all trademark symbols such as ®©™ from your products’ descriptions while keeping punctuation, you would use SUBSTITUTE. To remove all special characters and symbols including punctuation, use CLEAN_TEXT.

Example: PXM Industries™: New Neck Pillows! Only $13.40

If we apply CLEAN_TEXT to the Short Description above, we would get the following output:

Example formula:

```text
CLEAN_TEXT(VALUE(‘Short Description’))
```

Output: PXM Industries New Neck Pillows Only 13.40

Applying SUBSTITUTE requires you to specify every character you would like to replace along with their substitutes. To remove the special characters from our example, we would use “” as the substitution. Note that when using SUBSTITUTE, every character replacement must have a corresponding substitution listed directly after it in the formula.

Example formula:

```text
SUBSTITUTE(VALUE(‘Short Description’), “™”, “”, “®”, “”, “©”, “”)
```

Output: PXM Industries: New Neck Pillows! Only $13.40

Visit the Cheat Sheet for syntax, usage and examples for [CLEAN_TEXT](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-clean-text) and [SUBSTITUTE](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-substitute).

## Using JOIN_RELATIONS to return a set of related products

**Functions used:** [`JOIN_RELATIONS`](salsify-functions.md#join-relations)

With `JOIN_RELATIONS`, you can pull out all the related product IDs for any given relations label. In this example, we want to return all the products stored in the "Also Bought" relation, and return them as a comma-separated list. This product has two relations stored, IDs `112616` and `161409`.

For this example, the formula is:

```text
JOIN_RELATIONS("Also Bought",",")
```

To use this example, replace `Also Bought` with the name of your relation type, and update the separator if you want to use something other than a comma.

The previewed result in the image below returned the two comma-separated product IDs.

To use this formula, replace `Also Bought` with the label for your relation, and the last comma with whatever separator you want between the product IDs.

## Replace and Remove Characters with Regular Expressions

**Functions used:** [`REPLACE`](salsify-functions.md#replace), [`VALUE`](salsify-functions.md#value), [`VALUES`](salsify-functions.md#values)

In cases where you need to perform a more precise replacement or removal of certain characters, you can use regular expressions (regex) in formulas. The `REPLACE` function is similar to `SUBSTITUTE`, but it allows you to use regex to make your replacements.

You can use `REPLACE` on individual values you pull from Salsify properties, fixed values, and arrays of values.

`REPLACE("source_value", "regex", "replacement_value")`

The syntax is to provide the source value, or the value you want to make replacements in, then the regex which tells Salsify the kind of replacements to make, and then the value you want to insert in the original value as the replacement. Salsify formulas use Ruby syntax for regex.

For special characters, refer to hex codes in your regex.

### References

For help with regular expressions, here are a few external help sources:

- [Regex commands cheat sheet](https://www.cheatography.com/doublehelix/cheat-sheets/the-complete-regex/)
- [List of hex codes](https://www.ascii.cl/htmlcodes.htm)
- [Testing your regex](http://rubular.com/)

Here are some examples of ways you can use regex to make replacements in your values.

### Formulas in Action

#### Remove all special characters

In cases where you need to strip out all special characters from a value, `REPLACE` uses regex to do so. The formula below will replace everything except what's in the bracketed list.

Check the preview results carefully after you've done a replace to ensure that you're removing just the characters you've intended to.

To use this formula, replace `your-property-id` with the ID for the property you want to remove characters from.

```text
REPLACE(VALUE("Brand"), "[^A-Za-z0-9()$!@#%^&*+=_,/\'\":;?\\s\n.-]", "")
```

In the example above, square brackets `[]` indicate an array of values for the formula to evaluate. The carat `^` inside the brackets indicates that everything inside that list should not be replaced. In this example, we've chosen to keep alpha-numeric characters (`A-Za-z0-9`), punctuation marks and other commonly-used symbols in text, character returns (`\n`), and spaces (`\s`). Some special punctuation characters need to be escaped with a forward slash `\` to be processed correctly by the formula editor. You could add other characters to the list inside the square brackets in the formula that you want to retain. Because of the way the statement is processed, the dash character (`-`) needs to appear last in the list.

#### Remove all non-digit characters

Will remove all characters that are not numbers regardless of their position. More efficient than `SUBSTITUTE`, and you don’t have to know the included characters to remove them. Note that in this example, decimal points included in numbers would also be removed.

To use this example, replace your-property-id with the ID for your property.

##### From a property value

```text
dir="ltr">REPLACE(VALUE("your-property-id"), "\\D+", "")
```

With this formula, if the value we have stored in your-property-id is pi = 3.14 the formula output would be 314.

##### From an array

```text
REPLACE(["pi=3.14","regex is 4 u"], "\\D+", "")
```

This formula will return two values: 3.14 and 4.

#### Replace strings over a certain length

This formula will evaluate your property value and if it’s over the specified length, it will replace it with the second value you specify. Useful in cases where you have varying lengths content and you want to use the one that best meets a retailer’s maximum length.

For example, if you store two versions of your product description, you can specify the max length the retailer allows, specify your longer description as the source and the shorter as the replacement. Then where the longer description meets the requirement it will be used, and where the shorter is needed, it will be used.

To use this example, replace Long Description with your primary value, 100 with the length you want to use, and Medium Description with the secondary value you want to replace the primary with if it’s over the specified length.

```text
REPLACE(VALUE("Long Description"), "^.{100,}", VALUE("Medium Description"))
```

In this example, if the value stored in Long Description is more than 100 characters, the value stored in Medium Description will be used.

#### Replace a value that appears between two characters or strings

In cases where you want to replace everything between two characters or strings, but don’t necessarily know what the text between those characters or strings will be, you can use:

```text
REPLACE("<propertyID>", "(?<=<)(.*)(?=>)", "<propertyID2>")
```

Where < is the starting character (or group of characters) and > is the ending character or group of characters.

This is useful, for example, when you want to change raw HTML tags in a block of text.

```text
REPLACE("<b>This text should not be bold</b>", "(?<=<)(.*)(?=>)", "i")
```

This expression will change the bolded text to italicized text by changing the HTML tags.

#### Replace multiple spellings of a word with a single spelling

This example is useful if you’re standardizing data to either meet a requirement, or in bulk edit. It allows you to find multiple spellings of a word (like “humor” and “humour”) and replace them with a single version.

To use this example, replace Keyword with your source property ID, hum(o|ou)r with the variations in spelling wrapped in parentheses and separated by a pipe, and the replacement value. The replacement is in parentheses with the replacement value first, and the value being replaced second.

```text
REPLACE(VALUE("Keyword"), "hum(o|ou)r", "o")
```

#### Replace multiple colors with a single color

In this example, three color values (aqua, periwinkle, #008080) stored in the property Color are being replaced with a single color, Blue. Note that replacements are case sensitive, so if Aqua were a stored value, it would not be replaced with Blue.

To use this example, replace Color with your property ID, replace aqua|periwinkle|#008080 with a pipe delimited group of your values to be replaced, and Blue with your replacement value.

```text
REPLACE(VALUE("Color"), "(aqua|periwinkle|#008080)", "Blue")
```

## Return an array of values

**Functions used:** [`COMPACT`](salsify-functions.md#compact), [`CONCATENATE`](salsify-functions.md#concatenate), [`STRIP_HTML`](salsify-functions.md#strip-html), [`SUBSTITUTE`](salsify-functions.md#substitute), [`VALUE`](salsify-functions.md#value), [`VALUES`](salsify-functions.md#values)

There are many cases where you need to return a group of values to an attribute. You can handle this in several ways depending on how you store your information. Review the following use cases and modify the examples to suit your circumstances.

##### Map to a single multi-value property

The simplest way to send an array is to map to a single property that contains the values you want to send. If you have a property you can map to directly, find the property name in the Existing Values section of the mapping drop down menu.

##### Map to an array of multi-value properties

If you need to pull from more than one property that have multiple values, you can use a formula like this:

```text
COMPACT(
CONCAT_ARRAYS(
VALUES("Bullet Points"),
VALUES("Feature Bullets")
)
)
```

`COMPACT` removes instances where you might have empty values, and `CONCAT ARRAYS` lists the values in each property in the order they are included in the formula. Replace `Bullet Points` and `Feature Bullets` with your Salsify property IDs. If you need to pull from more properties, add additional `VALUES` lines, separated by commas.

##### Map to multiple single-value properties

If your values are stored in separate properties, you can use this variation of the previous formula. Note that if any of the properties have multiple values, it will only pull the first. To pull multiple values from any group of properties, use the previous example.

Replace each `Bullet Point n` with your property IDs.

```text
COMPACT(
CONCATENATE(
VALUE("Bullet Point 1"),
VALUE("Bullet Point 2"),
VALUE("Bullet Point 3"),
VALUE("Bullet Point 4"),
VALUE("Bullet Point 5"),
VALUE("Bullet Point 6")
)
)
```

##### Mix property values with fixed text to create a list of values

You may have cases where you want to create a set of values from a stored piece of information. For example, you may have a property that contains the length of warranty like `Warranty Length` and you want a value that says "Features a 10 year warranty". Where your property only stores 10, create a value with `CONCATENATE`:

```text
CONCATENATE("Features a ",VALUE("Warranty")," year warranty")
```

Be mindful of where you need spaces in the sentence parts you're including. In this case we needed a space after the a and before year, since the value only stored 10 with no spaces.

Combine this with other formulas to add additional values. For example, if we were pulling from multiple single-value bullet points, you'd include this created value this way:

```text
COMPACT(
CONCATENATE(
VALUE("Bullet Point 1"),
CONCATENATE("Features a ",VALUE("Warranty")," year warranty"),
VALUE("Bullet Point 3"),
VALUE("Bullet Point 4"),
VALUE("Bullet Point 5"),
VALUE("Bullet Point 6")
)
)
```

In some cases formatting is stored in your Salsify values. You can remove the characters in one of the following ways:

##### Remove HTML formatting from a property

If your property includes bullet points with HTML, stored like this: `<li>This is a bullet point</li>`, you can remove the html with the `STRIP_HTML` function.

```text
STRIP_HTML(VALUE("Bullet Points"))
```

##### Remove a bullet point character from a property

If a bullet character, or other special characters, are stored in properties you want to use, you can use `SUBSTITUTE` to remove them.

```text
SUBSTITUTE(
#the location of the values you want to remove characters from
VALUE("Bullet Points"),
#comma-separated values: "character to change", "replacement character"
"•",""
)
```

In this formula, we're replacing the bullet character with a blank. If you need to remove additional characters, add a comma at the end of the comma-separated line and add another for each character to replace.

## Round to a Specific Number of Digits After a Decimal Point

**Functions used:** [`ROUND`](salsify-functions.md#round), [`VALUE`](salsify-functions.md#value)

How you want to handle rounding for the final value will determine the function you want to use to limit digits after a decimal point. You can use one of three functions to meet the requirement. `ROUND` is the most commonly-used function to solve this mapping challenge. Please see the cheat sheet for usage of each function.

[ROUND](https://help.salsify.com/ProductXM/s/article/salsify-formula-round) - Will round with traditional rounding logic to the number of digits specified. Remainder under 5 will round down, 5 and over will round up. This is the most commonly-used function to meet this type of requirement.

[MROUNDUP](https://help.salsify.com/ProductXM/s/article/salsify-formula-mroundup) - Will round up in specified increments. So for example, you could round up to a remainder that always ends in 5. Or if you just want to force the logic to always round up, you could set the increment to 1.

[LTRIM](https://help.salsify.com/ProductXM/s/article/salsify-formula-ltrim) - Limits the number of overall characters in the value and doesn't perform any rounding.

**Property ID & Name: **Cost
**Value Stored: **19.992222

In this case we have 6 digits after the decimal and we need to round to 2. The following formula will achieve the result. To use this formula, copy it and replace Cost here in blue with the property ID that stores the value you want to round.

```text
ROUND(VALUE('Cost'), 2)
```

The result will be 19.99

## Sending pairs of label and value information with COMPOUND

There are some cases where a readiness report requires that you send pairs of data, a label and a value, separated by a colon. Use COMPOUND to send this information.

For example, there may be an attribute that requires that you send labels and values that describe in what aspects a product varies like `color: red`, and `size: M`

With COMPOUND, you specify the labels and values in pairs. You can include a series of pairs, and they’ll be formatted as an array of pairs of values.

[Visit the Cheat Sheet](https://help.salsify.com/ProductXM/s/article/salsify-formula-compound) for syntax, usage and examples for COMPOUND.

## Setting a default value & returning a value from a set of properties with COALESCE

**Functions used:** [`COALESCE`](salsify-functions.md#coalesce), [`VALUE`](salsify-functions.md#value)

There are cases when you're mapping where you need to set a single value for most of your products, or you need to fill in a default value where data might be missing in an attribute.

For example, PXM Industries is sending a set of products to The Home Depot, and they have an attribute to specify the house brand the products are sold under. PXM Industries stores Home Depot's private brand name for the products it pertains to, but for all others, we need to specify ".N/A" in the readiness report.

For this instance, we can set up a formula that looks at the property we store the private brand in, and if it's empty, we'll fill in ".N/A". There are a few ways we could do this, like test for a value with a series of `IF`/`OR`/`AND`/`EQUAL` formulas.

But for this case, `COALESCE` is the most straightforward. It works like this:

To use this formula as it is, replace the portion in blue with your property ID, and the portion in orange with your default value.

```text
COALESCE(VALUE('The Home Depot Private Brand'),'.N/A')
```

This formula checks the series of values you include and returns the one that matches first. So in this case, it looks in the property "The Home Depot Private Brand" and if it exists it returns that value. If it doesn't, it returns the next which is a fixed value of .N/A

You can check multiple properties with this formula to create a longer series as well. So for example if you have several different versions of marketing content, you can check the one that's most relevant to the requirement, then the next most relevant, then the next and as many as you like until you're complete. You can choose whether or not to end with a default value or not.

In this example, we're checking first the long description for a product, then the medium description, then the short description. If none of those exist, we'll leave the attribute blank.

```text
COALESCE(VALUE('Long Description'),VALUE('Medium Description'),VALUE('Short Description'))
```

Again this formula goes in order and looks at each property and if there's a value, it returns the first it finds and stops. So if a product had a Medium and Short description, it would return only the Medium one. If all three were empty, no value would be returned.

## How to use Universal Properties with Salsify Formulas

**Applies to**:

- PXM Advance only
- Universal Properties
- Channel Mapping with Salsify Formulas

#### What are Universal Properties?

See: [[PXM Advance] Universal Properties](https://help.salsify.com/ProductXM/s/article/universal-properties)

#### How are Universal Properties used?

- The [Grocery Content Quality Workflow](https://help.salsify.com/ProductXM/s/article/grocery-content-quality-workflow) uses Universal Properties to determine which product information to review.

- [Nutrient Facts Label Visualization](https://help.salsify.com/ProductXM/s/article/nutrition-label-visualization) uses Universal Properties to determine which product information to include in the label image.

- When you set up a new channel for the [Salsify Open Catalog](https://help.salsify.com/ProductXM/s/article/salsify-open-catalog) or the [Kroger Direct Connection](https://help.salsify.com/ProductXM/s/article/kroger-direct-connection), you can automatically apply your Universal Properties to the channel attributes by contacting Customer Support.

#### Universal Property example

In this section, we’ll walk through setting up a Universal Property for Calorie quantity. We’ll use this in the formula examples in the next sections.

##### Step 1: Set up a standard property

In my Salsify organization, I've created a property named “Calories”. The property has a “number” data type. I’ll use this property to store quantity values. In the screenshot below, you can see the details for the “Calories” property in the Properties menu.

##### Step 2: Associate the standard property to a Universal Property

I worked with a Salsify Implementation Consultant or Salsify partner to [import Universal Property associations](https://help.salsify.com/ProductXM/s/article/universal-properties#how-to-import-universal-property-associations). We set the “Calories” property as the source for the Universal Property:

“nutritionalFacts.UNPREPARED.BY_SERVING.nutrientDetail.ENER-.quantityContained.value”.

I can [export and review my Universal Property associations](https://help.salsify.com/ProductXM/s/article/universal-properties#how-to-export-universal-property-associations) from the *Manage this Organization > Data* menu. The screenshot below shows the “Calories” property in the Universal Property association export.

##### Step 3: Import values to the standard property

Next, I imported values to the “Calories” property for my products. In the screenshot below, you can see an example of a product detail page with a value for the “Calories” property.

#### Return a value with the UNIVERSAL_PROPERTIES function

You can use the UNIVERSAL_PROPERTY formula function to return a value stored in the property associated to a Universal Property.

For example, I can use the UNIVERSAL_PROPERTY function with the Universal Property ID: “nutritionalFacts.UNPREPARED.BY_SERVING.nutrientDetail.ENER-.quantityContained.value” to return the value stored in my “Calories” property.

If I use a different level of the Universal Property ID, I can return a collection instead of a value. For example, if I remove “.value” from the ID, I can return a collection where “value” is the key.

Learn more:

- Formulas Cheat Sheet: [UNIVERSAL_PROPERTIES](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-universal-properties)
- [Working with Collections](https://help.salsify.com/ProductXM/s/article/working-with-collections)

#### **Use Universal Properties with other formula functions**

Some Salsify formula functions allow you to use a Universal Property ID instead of a standard property ID. For example, I can use the Universal Property ID with the VALUE function to return the value stored in the Calories property.

For these functions, you will need to add a prefix of “salsify:universal:” before the Universal Property ID:

salsify:universal:nutritionalFacts.UNPREPARED.BY_SERVING.nutrientDetail.ENER-.quantityContained.value

Salsify formula functions that support Universal Property IDs:

- [VALUE](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-value)
- [VALUES](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-values)
- [LOCALIZED_VALUE](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-localized-value)
- [LOCALIZED_VALUES](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-localized-values)
- [REFERENCED_VALUE](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-referenced-value)
- [REFERENCED_VALUES](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-referenced-values)
- [LOCALIZED_REFERENCED_VALUE](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-localized-referenced-value)
- [LOCALIZED_REFERENCED_VALUES](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet#salsify-formula-localized-referenced-values)

## Working with Arrays

**Functions used:** [`ADD`](salsify-functions.md#add), [`IF`](salsify-functions.md#if), [`IN`](salsify-functions.md#in), [`JOIN`](salsify-functions.md#join), [`LENGTH`](salsify-functions.md#length), [`SLICE`](salsify-functions.md#slice), [`VALUE`](salsify-functions.md#value), [`VALUES`](salsify-functions.md#values)

An array is a list of multiple values in a specific order. Any property in Salsify can have multiple values, and as in the example above you can use the `VALUES` formula to output an array of a property’s values. In addition to the `VALUES` formula there are other ways to generate arrays.

### Value Arrays from Multi-value Properties

For properties with multiple values, use `VALUES` to return the array of values rather than `VALUE`, which by default returns only the first value in the property. You can add two optional parameters to return values starting at a specific position in the array, like the second or third value in the list. And you can limit the number of values the formula returns.

For example, if we have a property called *Tags* with the following values:

- backpack
- school
- travel bag

With the formula `VALUE("Tags")`, the result would be the first value in the property:

#### Return All Values in a Multi-Value Property

With the formula `VALUES("Tags")`, the result would be all values in the property are returned, separated by line breaks:

#### Return Values from a Specific Starting Position

You can return all the values from a specific starting position forward by specifying an index. So in this example, if you want to return everything from the second position on, your formula would be:

`VALUES("Tags",2)`

In this example, you're starting at position two, and returning all the rest of the values.

#### Return a Maximum Number of Values

You can also choose to limit the number of values to return. So for example, if you store 10 values, and your retailer only accepts a maximum of 2, you can set the maximum and choose where the starting point is to return from.

`VALUES("Tags",3,2)`

This formula will return the 3rd and 4th value stored in the property. The first number in the formula sets the starting point, and the second sets the maximum number of values to return. Keep in mind, that if you don't have values in the positions you've specified you may not get the result you expect. In our example, we only have three values stored for the product. So the formula only returns the value in the 3rd position.

If you want to return the first two values, set the index at 1 and the limit at 2. If there's only one number in the formula, it's treated as the index.

`VALUES("Tags",1,2)`

### Pull Values from an Array of Properties

Adding square brackets around values creates an array.

`[VALUE("propertyID1"), VALUE("propertyID2"), VALUE("propertyID3")]`

You can take an array of values and produce a single string (text) value by joining elements of an array with a delimiter as below. Either of these examples will output all values from each property, and insert a new line between values.

`JOIN([VALUE("propertyID1"), VALUE("propertyID2"), VALUE("propertyID3")], "")`

`JOIN([VALUE("propertyID1"), VALUE("propertyID2"), VALUE("propertyID3")], "\n")`

### Test for Existence of a Specific Value in a Multi-value Property

You can evaluate an array for the existence of a specific value and either take action based on it, or return an array of true/false values. In this use case, use `IN` to check for a value and return a true/false result, or combine with `IF` to take action based on the true/false status.

```text
IF(IN(VALUES("your-property-id"),"value to test for"),"action if true","action if false")
```

In this at example, the formula evaluates an array of values stored in a multi-value property and if "value to test for" exists, it would return "action if true", and if not it would return "action if false". The evaluation is case sensitive, so if you're looking for "White", "white" would return false.

#### Test for Existence of a Specific Value in an Array of Single-value Properties

`IN` works in a similar way as the previous example for an array of properties. Use square brackets around your array of properties, and the formula will return true if the value exists in the array.

```text
IF(IN([VALUE("property-id-1"),VALUE("property-id-2"),VALUE("property-id-3")]),
"value to test for",
"action if true",
"action if false")
```

There are some cases where the readiness report requires a specific delimiter. Use `JOIN` to return multiple values and specify the delimiter between them.

With the formula `JOIN(VALUES("Tags"))` the result would be a comma-delimited list of all values in the property:

### Pull Values from an Array

In cases where you want to return only part of the values in a multi-value property, use SLICE to specify the property, which position to start pulling values from, and optionally, specify the maximum number of values to return. From our example above, let's say we want to not return the first value.

With the formula `SLICE(VALUES("Tags"),2)`, the result would be all values starting from position 2 would be returned.

If you need to specify a delimiter for the values, wrap the formula in JOIN and specify the delimiter.

With the formula `JOIN(SLICE(VALUES("Tags"),2)`, the result would be a comma-delimited list of the values starting at position 2.

If we want only the second value in the property to be returned, with the formula `SLICE(VALUES("Tags"),2,1)`, we specify to start at position 2 and only return 1 value, so only the value in position 2 would be returned.

### Return Length of an Array

You can return the count of values in an array with `LENGTH`. Continuing the example above the product has three values stored, so this formula returns 3.

`LENGTH(VALUES("Tags"))`

### Arithmetic Functions & Arrays

You can use arrays to apply the same function across multiple values. In this example,

`ADD(2,[3,4,5])` adds 2 to each value and outputs:

5.0
6.0
7.0

See the [Formula Cheat Sheet](https://help.salsify.com/ProductXM/s/article/formulas-cheat-sheet) for the full list of Salsify Formulas.

## Working with Collections

**Functions used:** [`COLLECTION`](salsify-functions.md#collection), [`COMPOUND`](salsify-functions.md#compound), [`EACH_PAIR`](salsify-functions.md#each-pair), [`VALUE_AT`](salsify-functions.md#value-at)

A collection is an ordered set of key-value pairs whose values may be accessed by corresponding key, and whose key may be of almost any type. The COLLECTION and COMPOUND functions can be used to generate collections in formulas. Collections are generally used in channel mapping formulas for complex attribute collection fields, but may be combined with other functions for further use-cases.

The COLLECTION and COMPOUND functions behave similarly by generating a collection from key-value pairs of information, provided as elements of an array:

```text
COLLECTION('quantity', '3', 'unit', 'grams')
```

and,

```text
COMPOUND('quantity', '3', 'unit', 'grams')
```

both return,

```text
{ "quantity": "3", "unit": "grams" }
```

The COMPOUND function however treats arrays differently, returning a collection for each combination of elements in the array with the provided key:

```text
COLLECTION('color', ['blue', 'green'])
#output => { "color": ["blue", "green"] }

COMPOUND('color', ['blue', 'green'])
#output => [{ "color": "blue" }, { "color": "green" }
```

Collections may be used in combination with other functions, such as VALUE_AT for retrieving values from collections by their key,

```text
LET col = COLLECTION('material', 'cotton') IN

VALUE_AT(col, 'material')
#output => 'cotton'
```

or EACH_PAIR for transforming key-value pairs,

```text
LET col = COLLECTION('color', 'blue', 'material', 'cotton') IN

EACH_PAIR(col, (key, value) => CONCAT(key, ' is ', value))
#output => ['color is blue', 'material is cotton']
```

The COMPOUND function is available everywhere besides digital asset renaming formulas, and the COLLECTION function is only available in templated export and readiness report formulas.
