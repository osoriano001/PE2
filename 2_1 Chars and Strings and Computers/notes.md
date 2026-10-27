# How computers understand single characters

- ASCII - American Standard Code for Information Interchange. Consists of 256 characters, but to understand human readable language focus on range 0 - 127 (hexidecimal <code>x00 - x7F</code>)

<table class="python-table" style="width:100%">
<tbody>
</tbody><thead><tr>
<th style="background-color:#3d5368;color:white; padding:5px;">Character</th>
<th class="python-table">Code</th>

<th>Character</th>
<th>Code</th>

<th>Character</th>
<th>Code</th>

<th>Character</th>
<th>Code</th>
</tr></thead>
<tbody><tr>
<td>(NUL)</td>
<td>0</td>

<td>(space)(&nbsp;)</td>
<td>32</td>

<td>@</td>
<td>64</td>

<td>`</td>
<td>96</td>
</tr>
<tr>
<td>(SOH)</td>
<td>1</td>

<td>!</td>
<td>33</td>

<td>A</td>
<td>65</td>

<td>a</td>
<td>97</td>
</tr>
<tr>
<td>(STX)</td>
<td>2</td>

<td>"</td>
<td>34</td>

<td>B</td>
<td>66</td>

<td>b</td>
<td>98</td>
</tr>
<tr>
<td>(ETX)</td>
<td>3</td>

<td>#</td>
<td>35</td>

<td>C</td>
<td>67</td>

<td>c</td>
<td>99</td>
</tr>
<tr>
<td>(EOT)</td>
<td>4</td>

<td>$</td>
<td>36</td>

<td>D</td>
<td>68</td>

<td>d</td>
<td>100</td>
</tr>
<tr>
<td>(ENQ)</td>
<td>5</td>

<td>%</td>
<td>37</td>

<td>E</td>
<td>69</td>

<td>e</td>
<td>101</td>
</tr>
<tr>
<td>(ACK)</td>
<td>6</td>

<td>&amp;</td>
<td>38</td>

<td>F</td>
<td>70</td>

<td>f</td>
<td>102</td>
</tr>
<tr>
<td>(BEL)</td>
<td>7</td>

<td>'</td>
<td>39</td>

<td>G</td>
<td>71</td>

<td>g</td>
<td>103</td>
</tr>
<tr>
<td>(BS)</td>
<td>8</td>

<td>(</td>
<td>40</td>

<td>H</td>
<td>72</td>

<td>h</td>
<td>104</td>
</tr>
<tr>
<td>(HT)</td>
<td>9</td>

<td>)</td>
<td>41</td>

<td>I</td>
<td>73</td>

<td>i</td>
<td>105</td>
</tr>
<tr>
<td>(LF)</td>
<td>10</td>

<td>*</td>
<td>42</td>

<td>J</td>
<td>74</td>

<td>j</td>
<td>106</td>
</tr>
<tr>
<td>(VT)</td>
<td>11</td>

<td>+</td>
<td>43</td>

<td>K</td>
<td>75</td>

<td>k</td>
<td>107</td>
</tr>
<tr>
<td>(FF)</td>
<td>12</td>

<td>,</td>
<td>44</td>

<td>L</td>
<td>76</td>

<td>l</td>
<td>108</td>
</tr>
<tr>
<td>(CR)</td>
<td>13</td>

<td>-</td>
<td>45</td>

<td>M</td>
<td>77</td>

<td>m</td>
<td>109</td>
</tr>
<tr>
<td>(SO)</td>
<td>14</td>

<td>.</td>
<td>46</td>

<td>N</td>
<td>78</td>

<td>n</td>
<td>110</td>
</tr>
<tr>
<td>(SI)</td>
<td>15</td>

<td>/</td>
<td>47</td>

<td>O</td>
<td>79</td>

<td>o</td>
<td>111</td>
</tr>
<tr>
<td>(DLE)</td>
<td>16</td>

<td>0</td>
<td>48</td>

<td>P</td>
<td>80</td>

<td>p</td>
<td>112</td>
</tr>
<tr>
<td>(DC1)</td>
<td>17</td>

<td>1</td>
<td>49</td>

<td>Q</td>
<td>81</td>

<td>q</td>
<td>113</td>
</tr>
<tr>
<td>(DC2)</td>
<td>18</td>

<td>2</td>
<td>50</td>

<td>R</td>
<td>82</td>

<td>r</td>
<td>114</td>
</tr>
<tr>
<td>(DC3)</td>
<td>19</td>

<td>3</td>
<td>51</td>

<td>S</td>
<td>83</td>

<td>s</td>
<td>115</td>
</tr>
<tr>
<td>(DC4)</td>
<td>20</td>

<td>4</td>
<td>52</td>

<td>T</td>
<td>84</td>

<td>t</td>
<td>116</td>
</tr>
<tr>
<td>(NAK)</td>
<td>21</td>

<td>5</td>
<td>23</td>

<td>U</td>
<td>85</td>

<td>u</td>
<td>117</td>
</tr>
<tr>
<td>(SYN)</td>
<td>22</td>

<td>6</td>
<td>54</td>

<td>V</td>
<td>86</td>

<td>v</td>
<td>118</td>
</tr>
<tr>
<td>(ETB)</td>
<td>23</td>

<td>7</td>
<td>55</td>

<td>W</td>
<td>87</td>

<td>w</td>
<td>119</td>
</tr>
<tr>
<td>(CAN)</td>
<td>24</td>

<td>8</td>
<td>56</td>

<td>X</td>
<td>88</td>

<td>x</td>
<td>120</td>
</tr>
<tr>
<td>(EM)</td>
<td>25</td>

<td>9</td>
<td>57</td>

<td>Y</td>
<td>89</td>

<td>y</td>
<td>121</td>
</tr>
<tr>
<td>(SUB)</td>
<td>26</td>

<td>:</td>
<td>58</td>

<td>Z</td>
<td>90</td>

<td>z</td>
<td>122</td>
</tr>
<tr>
<td>(ESC)</td>
<td>27</td>

<td>;</td>
<td>59</td>

<td>[</td>
<td>91</td>

<td>{</td>
<td>123</td>
</tr>
<tr>
<td>(FS)</td>
<td>28</td>

<td>&lt;</td>
<td>60</td>

<td>\</td>
<td>92</td>

<td>|</td>
<td>124</td>
</tr>
<tr>
<td>(GS)</td>
<td>29</td>

<td>=</td>
<td>61</td>

<td>]</td>
<td>93</td>

<td>}</td>
<td>125</td>
</tr>
<tr>
<td>(RS)</td>
<td>30</td>

<td>&gt;</td>
<td>62</td>

<td>^</td>
<td>94</td>

<td>~</td>
<td>126</td>
</tr>
<tr>
<td>(US)</td>
<td>31</td>

<td>?</td>
<td>63</td>

<td>_</td>
<td>95</td>
<td>&nbsp;</td>


<td>127</td>
</tr>
</tbody>
</table>


# I18N (Internationalization)

## Code points and code pages
- ASCII works for latin alpha-numeric characters and suffices with 127 code points of numbers correlating to different characters, but does not encapulate other languages well.

### Unicode
- Unicode assigns unique (unambiguous) characters (letters, hyphens, ideograms, etc.) to more than a million code points.

### UCS-4 (Universal character set)
- A general standard of how to implement unicode within computer memory
- Uses 32 bits (4 bytes). A file containing UCS-4 encoded text may start with a BOM (byte order mark), an unprintable combination of bits announcing the nature of the file's contents. Some utilities may require it.


### UTF-8 (Unicode Transformation Format)
- Uses as many bits for each of the code points as it really needs to represent them.
- No need to use the BOM, but some of the tools look for it when reading the file, and many editors set it up during the save.


