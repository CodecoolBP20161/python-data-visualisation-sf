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

## Class methods

None


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

object_list, width=600, height=600, background_color="#fff", font="arial_narrow_7.ttf"
 (more spec later)
#### Return value
None

### ```drawing```
Draw the tagcloud, + save and show it.

#### Arguments

None
#### Return value
None

### ```_word_list```
Make a dictionary with the texts and its attributes from the objects of a query

#### Arguments
None

#### Return value
None

### ```_overlap```
Check the overlap of texts

#### Arguments
position, width, height of the current text

#### Return value
None

## Static methods

None
