# TagCloud

## Description
This class represents the TagCloud picture.

## Parent class
None

## Attributes

* ```width```
  * data type: string
  * description: stores the width of the picture
* ```height```
  * data type: integer
  * description: stores the height of the picture
* ```image```
   * data type: object
   * description: the tagcloud image
* ```draw```
   * data type: class
   * description: store a class method of the ImageDraw class
* ```words```
   * data type: list
   * description: stores the texts and its properties for drawing
* ```font```
   * data type: string
   * description: stores the font_type of the tagcloud
* ```object_list```
   * data type: list
   * description: stores the object of a query
* ```_check_window_occupation```
   * data type: boolean
   * description: check if the window occupation OK

## Class methods

None


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
* ```object_list```
  * data type: list
  * description: stores the objects from the query
* ```width```
  * data type: integer
  * description: width of the window
* ```height```
   * data type: integer
   * description: height of the window
* ```background_color```
   * data type: string
   * description: stores the RGBA value of the background color
* ```font```
   * data type: string
   * description: store the filename of the font
#### Return value
None

### ```drawing```
Draw the tagcloud, + save and show it.

#### Arguments
* ```file_name```
   * data type: string
   * description: store the filename to save
#### Return value
None

### ```_word_list```
Make a dictionary with the texts and its attributes from the objects of a query

#### Arguments
* ```font_size_calculator```
   * data type: int
   * description: a vlaue for font_size calculations

#### Return value
None

### ```_overlap```
Check the overlap of texts

#### Arguments
* ```width```
  * data type: integer
  * description: width of the text
* ```height```
   * data type: integer
   * description: height of the text
* ```position```
   * data type: tuple
   * description: stores the x, y coords of the text

#### Return value
None

### ```_is_window_large```
Check if the window is too large

#### Arguments
None

#### Return value
True or False

### ```_check_tag_borders```
Calculate the Tag Cloud borders

#### Arguments
None

#### Return value
tuple with the (x_max, x_min, y_max, y_min)

### ```_crop_blank```
Crop the blank background

#### Arguments
None

#### Return value
None

## Static methods

None
