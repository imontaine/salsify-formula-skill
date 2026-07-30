# Variables to Streamline Salsify Formulas

Source: Salsify "Variables to Streamline Salsify Formulas"
Source last modified: May 27, 2025
Extracted: July 30, 2026

**Related references:** [`LET...IN`](salsify-functions.md#let-in) | [Function reference](salsify-functions.md) | [Common use cases](salsify-common-use-cases.md)

> **Compatibility note:** This May 2025 article says variables are supported in Readiness Report formulas and Templated Exports. The newer June 2026 Formulas Cheat Sheet lists `LET...IN` as compatible with additional formula contexts. Use the newer function reference when compatibility differs.

**Documented functions used:** [`ADD`](salsify-functions.md#add), [`CONCATENATE`](salsify-functions.md#concatenate), [`EACH`](salsify-functions.md#each), [`IF`](salsify-functions.md#if), [`JOIN`](salsify-functions.md#join), [`MID`](salsify-functions.md#mid), [`PROPER`](salsify-functions.md#proper), [`STRIP_HTML`](salsify-functions.md#strip-html), [`VALUE`](salsify-functions.md#value), [`VALUES`](salsify-functions.md#values)

**Additional formula names appearing in this article:** `CONCAT`, `LEFT`, `RIGHT`. These do not have standalone entries in the extracted June 2026 cheat sheet.

*Variables are supported in Readiness Report formulas and Templated Exports.*

Variables are used to store information to be referenced later in a Salsify formula. They provide a way of labeling data with a descriptive name, so formulas can be easier to understand. Using variables can also simplify otherwise very complex formulas.

## Where to Use Variables

Variables are handy ways to streamline calculations in formulas, and create shorter references to values to make formulas easier to build and edit.

In this example, we need to create a short product description, and the content is stored in three separate properties. We want to consolidate the bullet points into a paragraph with spaces between the bullets, and include information from the warranty field and the product line. Each property needs separate data transformations, and we need to test the properties to ensure there are values populated to them before we apply the transformations. To do this without variables, the formula would look like this:

```text
CONCATENATE(
  IF(
    VALUE("Bullet Points"),
    JOIN(VALUES("Bullet Points")," ")),
    " ",
  IF(
    VALUE("Warranty"),
    CONCATENATE(
      STRIP_HTML(VALUE("Warranty")),
      " warranty. "
      )
    ),
    " ",
  IF(
    VALUE("Product Line"),
    CONCATENATE(
      "From our ",
      VALUE("Product Line"),
      " product line."
    )
  )
)
```

With variables, the formula is streamlined to:

```text
let points = JOIN(VALUES("Bullet Points")," ") in
let war = EACH(VALUES("Warranty"), warrant => CONCATENATE(STRIP_HTML(warrant)," warranty",". ")) in
let line = EACH(VALUES("Product Line"), line => CONCATENATE("From our ",line," product line. ")) in

CONCATENATE(points," ",line,war)
```

The variables `points`, `war`, and `line` are defined here and hold the values to use in the main formula. Now the main formula just refers to the variables, and the `EACH` formulas also contain variables, eliminating the need for repeated `IF` statements.

[Learn more about using `EACH`](https://help.salsify.com/ProductXM/s/article/advanced-formulas#each).

## Using Variables

Variables in the Salsify formula language are assigned using the ‘let ... in’ syntax. To define a variable you must provide a name for the variable and a value. For instance, if you want to assign 1 to the variable `X`, you would write `let X = 1 in`
Be mindful of the following when using variables.

Variables:

- Must always be declared before they are used in a formula. Best practice is to declare them at the top of your formula wherever possible.
- Cannot have spaces in their names.
- Are denoted in red in the formula editor.
- Are case sensitive. For example, the variable `N` is a different from `n`.
- Hold the last value for which they were defined. Assigning a value to a variable twice will remove the first value and overwrite it with the last.

> **Warning:** Assigning a new value to the same variable will overwrite the old value.

```text
let x = 1 in
let x = ADD(x,x) in
CONCAT("Num", x)
```

Would return `Num2.0` rather than `Num1.0` and any subsequent references to `x` would return `2.0`.

You can use variables to set fixed values, or to perform functions before other functions are applied. For example:

### Fixed value variable

You can use a variable to stand in for a longer value like this simple example:

```text
let x="Product" in
let y="Name" in
CONCATENATE(x," ",y)
```

The result would be Product Name for every product.

### Function variable

Variables can also store the value of a formula result, which can help avoid nesting many formulas within each other.

In this example, we’ll use more descriptive variables, which can be helpful to identify them in more complex formulas. We’re pulling the values for properties in each variable, and because `Brand` is stored in all capital letters, we’re transforming it to proper case.

```text
let name=VALUE("Product Name") in
let brand=PROPER(VALUE("Brand")) in
CONCAT(brand," ",name)
```

The result here will be that each product will show its `Brand` value in proper case (first letter capitalized), followed by a space then its `Product Name` value. So if the `Brand` is WILDFLOWER and the `Product Name` is Jetsetter Carry On Roller - Fuschia, the result is Wildflower Jetsetter Carry On Roller - Fuschia.

### Date-formatting variables

In this example, we're reformatting to deliver `Active Date` in a retailer's required format. In Salsify, dates are stored as *YYYY-MM-DD*, and the retailer wants to receive *month/day/year*. The formula uses three variables to store pieces of the `Active Date` property value, and the formula will assemble them to meet the requirement.

In this case we also use an `IF` statement to test whether there is a value for `Active Date` before assembling them. If there is no value for the *year* variable, the formula will return a null result.

```text
#define variables
let year = LEFT(VALUE("Active Date"), "4") in #store left 4 digits of Active Date as year
let month = MID(VALUE("Active Date"), "6", "2") in #store the 2 digit month
let day = RIGHT(VALUE("Active Date"), "2") in #store right 2 digits of Active Date as day

#formula
IF(year,CONCATENATE(month,"/",day,"/",year)) #If year value exists, assemble date parts with separators to output month/day/year.
```
