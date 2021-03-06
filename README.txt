Metro.css
Creates a neat custom timeline stylized like a metro map. Sample can be seen here.

--

Prerequisites
Must have python installed.

--

Usage
1. Create a data sheet using the markup rules specified below in a simple .txt format
2. Run the following command:

       metro.py [Your Data Sheet] [Output HTML File]

   where [Your Data Sheet] is the document you created in the last step and [Output HTML File] is the specified name of the html file
3. Open your output html file to ensure the timeline is correct. Occasionaly glitches can occur. To fix mistakes, simply edit the data sheet and run the python command listed above again.
4. Once you're done, use your output html file anywhere
Markup Rules

A timeline can have a maximum of 3 concurrent lines, though line colors can change at any time. Lines must be specified in the following order:
1. Timeline bounds
2. Left Line
3. Right Line
4. Center Line
Each line (and the timeline bounds) are seperated by a line of hyphens (the length does not matter). Thus, the order is actually
1. Timeline bounds
2. ###########
3. Left Line
4. ###########
5. Right Line
6. ###########
7. Center Line
8. ###########
If a line ends before another, or is created after another line, the order is the same. Whitespaces can be used to position lines before/after others start. If a line ends and then begins again in the same position (left, for instance), a whitespace line segment must be used in between the end of the first line and the begining of the second. An example of this can be seen in the sample file.

The timeline bounds are a simple one-line declaration of the begining and end dates of the timeline ruler displayed on the left of the page. For example, a timeline begining in 2009 and ending in 2015 would be declared as

    2009:2015

Timeline bounds can currently only be declared in terms of years. However, quarter years may also be used. The following decimals can extend the timeline bounds without adding another year

.0 - Adds another tick for the next year (Not shown by default)
.25 - Adds ticks up to March of that year
.5 - Adds ticks up to June of that year
.75 - Adds ticks up to September of that year

For example, to display tick marks up to June of 2018, the following command is acceptable

    2009:2018.5

For any line, the basic order of code is the following:

1. Define the line color and length before the next station
2. Define the station and its title/subtitle
3. Define any junctions present at that station

Each step contains declarations. Each declaration must be written on a seperate line, though steps can contain more than one declaration. 

Step 1

Each line must have a color, and the color is defined in this step. The declaration of a Purple line of length 250 pixels is

    purple:250

After the initial declaration of color, the user does not need to specify again what the line color is in subsequent steps. Thus, the following line segment of length 175 would be

    :175

Declaring the line color again in another step will result in a color gradient for that line segment from the intial line color to the new one. For example, if the line color was originally declared as "Red", but the redeclared as "Blue" in a later step, that line segment with the redeclaration would be colored as a Red-Blue gradient. This can be seen in the sample file.

The following colors are available for use: Red, Pink, Orange, Black, Gray, Blue, Green

Lines may have adjacent lines running as well. For example, a Red line may have a Blue line on the left and a Green line on the right. To declare a segment like this with a length of 400, the code would be

    blue::green:400

("Red" is excluded as it was declared previously as the line color) Like before, once adjacent lines are declared the first time, they do not need to be declared again. To declare an individual adjacent line, say a blue line on the left, just remove the other colors as shown

    blue:::400

If you would like to remove a line, simple declare the above again without the color you want to remove. To remove the blue line in the above example, the code would be

    :red:green:400

Notice how the colons stay. If the same were to happen to the green line, the code would be no different

    :red::400

To create a whitespace line segment, use a hyphen instead of a color. For example, to declare a whitespace line segment of 100, write

    -:100

Remember, if you have adjacent lines, they will not be cleared as expected. For a line with two adjacent lines, the following command would be the equivalent to the above command

    -:-:-:100

For dotted lines, the command is two colons followed by the length. So for a dotted line of length 325, the command would be

    ::325

Step 2

Station titles are simply the title surrounded by quotation marks. The following command declares a station named "Grand Central"

    "Grand Central Station"

For subtitles, add a colon and then the subtitle. For the above station to have the subtitle "New York City" the code would be

    "Grand Central Station:New York City"

Step 3

Junctions can go to the left or right, can come up from the top or the bottom, and can fade or stay solid. To simple declare a junction facing right and down, the command would be

    >

The color of this junction line would be the color of the adjacent line of that side. If you had a Red line with a Pink line adjacent the right, this command would produce a pink junction line. For a junction facing left and down, the command would be

    <

Note: The adjacent line from which this junction line inherits its color is removed from the main line. To account for this, simply declare the adjacent line color again in Step 1 (after the junction command). If you do not have an adjacent line present on your current line, or would like to specify the color yourself, simply use

    <[color]:

for left junctions and

    >[color]:

for right junctions, where [color] is the color of your choice. To make the junction line fade out, insert "fade" into the command. For a green line fading down to the right, the command would be

    >green:fade:down

The same command can be used to make the green junction face up.

    >green:fade:up

If you don't want the line to fade, replace "fade" with "solid" in the above commands.

Up to four line junctions may be declared per station: up-left, up-right, down-left, down-right

--

Known Issues
Mostly just Internet Explorer. The CSS has been tested to work on most other major browsers, including desktop and mobile.

--

Questions/Bugs?
Contact Vicmart1 at gotovicmart@gmail.com

--

Copyright 2015 Vicmart Inc. All Rights Reserved
