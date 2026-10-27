# Comparing strings
Python strings can be compared using the same set of operators which are in use in relation to numbers: <code>==</code> <code>!=</code> <code>></code> <code>>=</code> <code><</code> <code><=</code>
It just compares code point values, character by character.

```python
'alpha' == 'alpha'
'alpha' != 'Alpha'
```
Output
```cmd
True
True
```
Comparing the first different character in both strings (keep ASCII/UNICODE code points in mind at all times.)
```python
'alpha' < 'alphabet'
'beta' > 'Beta'
```
Output
```cmd
True
True
```
If a string contains digits only, it's still not a number. It's interpreted as-is, like any other regular string, and its (potential) numerical aspect is not taken into consideration in any way.
```python
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')
```
Output
```cmd
False
True
False
True
True
```

**Comparing strings against numbers is generally a bad idea.**
The only comparisons you can perform with impunity are these symbolized by the <code>==</code> and <code>!=</code> operators. The former always gives False, while the latter always produces True.
```python
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
print('10' > 10)
```
Output
```cmd
False
True
False
True
TypeError exception
```

# Sorting
Comparing is closely related to sorting (or rather, sorting is in fact a very sophisticated case of comparing).
The first is implemented as a function named <code>sorted()</code>.
The second method affects the list itself – no new list is created. Ordering is performed in situ by the method named <code>sort()</code>.

```python
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()
# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
```
Output
```cmd
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']
```

# Strings vs. numbers
The number-string conversion is simple, as it is always possible. It's done by a function named <code>str()</code>.
Use the <code>int()</code> function if you want to get an integer, and <code>float</code>() if you need a floating-point value.

```python
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)
```
Output
```cmd
13 1.3
14.3
```

# Summary
1. Strings can be compared to other strings using general comparison operators, but comparing them to numbers gives no reasonable result, because no string can be equal to any number. For example:
   -   string <code>==</code> number is always <code>False</code>;
   -   string <code>!=</code> number is always <code>True</code>;
   -   string <code>>=</code> number always raises an exception.

2. Sorting lists of strings can be done by:
    -   a function named <code>sorted()</code>, creating a new, sorted list;
    -   a method named <code>sort()</code>, which sorts the list in situ
3. A number can be converted to a string using the <code>str()</code> function.

4. A string can be converted to a number (although not every string) using either the <code>int()</code> or <code>float()</code> function. The conversion fails if a string doesn't contain a valid number image (an exception is raised then).

5. ASCII Codepoint table:<br>
   **NOTE**: special characters -> numbers -> special characters -> capital letters -> special characters -> lower case letters
<table class="table table-ascii table-bordered table-border-ascii table-hover table-xs page-break">
    <thead>
    <tr class="table-header">
        <th class="col-plus"></th>
        <th class="col-40px">DEC</th>
        <th class="col-40px">OCT</th>
        <th class="col-40px">HEX</th>
        <th class="col-80px">BIN</th>
        <th class="col-50px">Symbol</th>
        <th class="col-110px">HTML Number</th>
        <th class="col-html">HTML Name</th>
        <th class="col-description" align="left">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr><td><button class="btn-index text-primary" title="Show more about code 32"><i class="icon-plus-square"></i></button></td><td><a href="/32" title="ASCII Code 32">32</a></td><td>040</td><td>20</td><td>00100000</td><td>SP</td><td>&amp;#32;</td><td>&nbsp;</td><td>Space</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 33"><i class="icon-plus-square"></i></button></td><td><a href="/33" title="ASCII Code 33">33</a></td><td>041</td><td>21</td><td>00100001</td><td>!</td><td>&amp;#33;</td><td>&amp;excl;</td><td>Exclamation mark</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 34"><i class="icon-plus-square"></i></button></td><td><a href="/34" title="ASCII Code 34">34</a></td><td>042</td><td>22</td><td>00100010</td><td>"</td><td>&amp;#34;</td><td>&amp;quot;</td><td>Double quotes (or speech marks)</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 35"><i class="icon-plus-square"></i></button></td><td><a href="/35" title="ASCII Code 35">35</a></td><td>043</td><td>23</td><td>00100011</td><td>#</td><td>&amp;#35;</td><td>&amp;num;</td><td>Number sign</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 36"><i class="icon-plus-square"></i></button></td><td><a href="/36" title="ASCII Code 36">36</a></td><td>044</td><td>24</td><td>00100100</td><td>$</td><td>&amp;#36;</td><td>&amp;dollar;</td><td>Dollar</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 37"><i class="icon-plus-square"></i></button></td><td><a href="/37" title="ASCII Code 37">37</a></td><td>045</td><td>25</td><td>00100101</td><td>%</td><td>&amp;#37;</td><td>&amp;percnt;</td><td>Per cent sign</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 38"><i class="icon-plus-square"></i></button></td><td><a href="/38" title="ASCII Code 38">38</a></td><td>046</td><td>26</td><td>00100110</td><td>&amp;</td><td>&amp;#38;</td><td>&amp;amp;</td><td>Ampersand</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 39"><i class="icon-plus-square"></i></button></td><td><a href="/39" title="ASCII Code 39">39</a></td><td>047</td><td>27</td><td>00100111</td><td>'</td><td>&amp;#39;</td><td>&amp;apos;</td><td>Single quote</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 40"><i class="icon-plus-square"></i></button></td><td><a href="/40" title="ASCII Code 40">40</a></td><td>050</td><td>28</td><td>00101000</td><td>(</td><td>&amp;#40;</td><td>&amp;lparen;</td><td>Open parenthesis (or open bracket)</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 41"><i class="icon-plus-square"></i></button></td><td><a href="/41" title="ASCII Code 41">41</a></td><td>051</td><td>29</td><td>00101001</td><td>)</td><td>&amp;#41;</td><td>&amp;rparen;</td><td>Close parenthesis (or close bracket)</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 42"><i class="icon-plus-square"></i></button></td><td><a href="/42" title="ASCII Code 42">42</a></td><td>052</td><td>2A</td><td>00101010</td><td>*</td><td>&amp;#42;</td><td>&amp;ast;</td><td>Asterisk</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 43"><i class="icon-plus-square"></i></button></td><td><a href="/43" title="ASCII Code 43">43</a></td><td>053</td><td>2B</td><td>00101011</td><td>+</td><td>&amp;#43;</td><td>&amp;plus;</td><td>Plus</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 44"><i class="icon-plus-square"></i></button></td><td><a href="/44" title="ASCII Code 44">44</a></td><td>054</td><td>2C</td><td>00101100</td><td>,</td><td>&amp;#44;</td><td>&amp;comma;</td><td>Comma</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 45"><i class="icon-plus-square"></i></button></td><td><a href="/45" title="ASCII Code 45">45</a></td><td>055</td><td>2D</td><td>00101101</td><td>-</td><td>&amp;#45;</td><td>&nbsp;</td><td>Hyphen-minus</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 46"><i class="icon-plus-square"></i></button></td><td><a href="/46" title="ASCII Code 46">46</a></td><td>056</td><td>2E</td><td>00101110</td><td>.</td><td>&amp;#46;</td><td>&amp;period;</td><td>Period, dot or full stop</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 47"><i class="icon-plus-square"></i></button></td><td><a href="/47" title="ASCII Code 47">47</a></td><td>057</td><td>2F</td><td>00101111</td><td>/</td><td>&amp;#47;</td><td>&amp;sol;</td><td>Slash or divide</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 48"><i class="icon-plus-square"></i></button></td><td><a href="/48" title="ASCII Code 48">48</a></td><td>060</td><td>30</td><td>00110000</td><td>0</td><td>&amp;#48;</td><td>&nbsp;</td><td>Zero</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 49"><i class="icon-plus-square"></i></button></td><td><a href="/49" title="ASCII Code 49">49</a></td><td>061</td><td>31</td><td>00110001</td><td>1</td><td>&amp;#49;</td><td>&nbsp;</td><td>One</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 50"><i class="icon-plus-square"></i></button></td><td><a href="/50" title="ASCII Code 50">50</a></td><td>062</td><td>32</td><td>00110010</td><td>2</td><td>&amp;#50;</td><td>&nbsp;</td><td>Two</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 51"><i class="icon-plus-square"></i></button></td><td><a href="/51" title="ASCII Code 51">51</a></td><td>063</td><td>33</td><td>00110011</td><td>3</td><td>&amp;#51;</td><td>&nbsp;</td><td>Three</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 52"><i class="icon-plus-square"></i></button></td><td><a href="/52" title="ASCII Code 52">52</a></td><td>064</td><td>34</td><td>00110100</td><td>4</td><td>&amp;#52;</td><td>&nbsp;</td><td>Four</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 53"><i class="icon-plus-square"></i></button></td><td><a href="/53" title="ASCII Code 53">53</a></td><td>065</td><td>35</td><td>00110101</td><td>5</td><td>&amp;#53;</td><td>&nbsp;</td><td>Five</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 54"><i class="icon-plus-square"></i></button></td><td><a href="/54" title="ASCII Code 54">54</a></td><td>066</td><td>36</td><td>00110110</td><td>6</td><td>&amp;#54;</td><td>&nbsp;</td><td>Six</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 55"><i class="icon-plus-square"></i></button></td><td><a href="/55" title="ASCII Code 55">55</a></td><td>067</td><td>37</td><td>00110111</td><td>7</td><td>&amp;#55;</td><td>&nbsp;</td><td>Seven</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 56"><i class="icon-plus-square"></i></button></td><td><a href="/56" title="ASCII Code 56">56</a></td><td>070</td><td>38</td><td>00111000</td><td>8</td><td>&amp;#56;</td><td>&nbsp;</td><td>Eight</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 57"><i class="icon-plus-square"></i></button></td><td><a href="/57" title="ASCII Code 57">57</a></td><td>071</td><td>39</td><td>00111001</td><td>9</td><td>&amp;#57;</td><td>&nbsp;</td><td>Nine</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 58"><i class="icon-plus-square"></i></button></td><td><a href="/58" title="ASCII Code 58">58</a></td><td>072</td><td>3A</td><td>00111010</td><td>:</td><td>&amp;#58;</td><td>&amp;colon;</td><td>Colon</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 59"><i class="icon-plus-square"></i></button></td><td><a href="/59" title="ASCII Code 59">59</a></td><td>073</td><td>3B</td><td>00111011</td><td>;</td><td>&amp;#59;</td><td>&amp;semi;</td><td>Semicolon</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 60"><i class="icon-plus-square"></i></button></td><td><a href="/60" title="ASCII Code 60">60</a></td><td>074</td><td>3C</td><td>00111100</td><td>&lt;</td><td>&amp;#60;</td><td>&amp;lt;</td><td>Less than (or open angled bracket)</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 61"><i class="icon-plus-square"></i></button></td><td><a href="/61" title="ASCII Code 61">61</a></td><td>075</td><td>3D</td><td>00111101</td><td>=</td><td>&amp;#61;</td><td>&amp;equals;</td><td>Equals</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 62"><i class="icon-plus-square"></i></button></td><td><a href="/62" title="ASCII Code 62">62</a></td><td>076</td><td>3E</td><td>00111110</td><td>&gt;</td><td>&amp;#62;</td><td>&amp;gt;</td><td>Greater than (or close angled bracket)</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 63"><i class="icon-plus-square"></i></button></td><td><a href="/63" title="ASCII Code 63">63</a></td><td>077</td><td>3F</td><td>00111111</td><td>?</td><td>&amp;#63;</td><td>&amp;quest;</td><td>Question mark</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 64"><i class="icon-plus-square"></i></button></td><td><a href="/64" title="ASCII Code 64">64</a></td><td>100</td><td>40</td><td>01000000</td><td>@</td><td>&amp;#64;</td><td>&amp;commat;</td><td>At sign</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 65"><i class="icon-plus-square"></i></button></td><td><a href="/65" title="ASCII Code 65">65</a></td><td>101</td><td>41</td><td>01000001</td><td>A</td><td>&amp;#65;</td><td>&nbsp;</td><td>Uppercase A</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 66"><i class="icon-plus-square"></i></button></td><td><a href="/66" title="ASCII Code 66">66</a></td><td>102</td><td>42</td><td>01000010</td><td>B</td><td>&amp;#66;</td><td>&nbsp;</td><td>Uppercase B</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 67"><i class="icon-plus-square"></i></button></td><td><a href="/67" title="ASCII Code 67">67</a></td><td>103</td><td>43</td><td>01000011</td><td>C</td><td>&amp;#67;</td><td>&nbsp;</td><td>Uppercase C</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 68"><i class="icon-plus-square"></i></button></td><td><a href="/68" title="ASCII Code 68">68</a></td><td>104</td><td>44</td><td>01000100</td><td>D</td><td>&amp;#68;</td><td>&nbsp;</td><td>Uppercase D</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 69"><i class="icon-plus-square"></i></button></td><td><a href="/69" title="ASCII Code 69">69</a></td><td>105</td><td>45</td><td>01000101</td><td>E</td><td>&amp;#69;</td><td>&nbsp;</td><td>Uppercase E</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 70"><i class="icon-plus-square"></i></button></td><td><a href="/70" title="ASCII Code 70">70</a></td><td>106</td><td>46</td><td>01000110</td><td>F</td><td>&amp;#70;</td><td>&nbsp;</td><td>Uppercase F</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 71"><i class="icon-plus-square"></i></button></td><td><a href="/71" title="ASCII Code 71">71</a></td><td>107</td><td>47</td><td>01000111</td><td>G</td><td>&amp;#71;</td><td>&nbsp;</td><td>Uppercase G</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 72"><i class="icon-plus-square"></i></button></td><td><a href="/72" title="ASCII Code 72">72</a></td><td>110</td><td>48</td><td>01001000</td><td>H</td><td>&amp;#72;</td><td>&nbsp;</td><td>Uppercase H</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 73"><i class="icon-plus-square"></i></button></td><td><a href="/73" title="ASCII Code 73">73</a></td><td>111</td><td>49</td><td>01001001</td><td>I</td><td>&amp;#73;</td><td>&nbsp;</td><td>Uppercase I</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 74"><i class="icon-plus-square"></i></button></td><td><a href="/74" title="ASCII Code 74">74</a></td><td>112</td><td>4A</td><td>01001010</td><td>J</td><td>&amp;#74;</td><td>&nbsp;</td><td>Uppercase J</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 75"><i class="icon-plus-square"></i></button></td><td><a href="/75" title="ASCII Code 75">75</a></td><td>113</td><td>4B</td><td>01001011</td><td>K</td><td>&amp;#75;</td><td>&nbsp;</td><td>Uppercase K</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 76"><i class="icon-plus-square"></i></button></td><td><a href="/76" title="ASCII Code 76">76</a></td><td>114</td><td>4C</td><td>01001100</td><td>L</td><td>&amp;#76;</td><td>&nbsp;</td><td>Uppercase L</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 77"><i class="icon-plus-square"></i></button></td><td><a href="/77" title="ASCII Code 77">77</a></td><td>115</td><td>4D</td><td>01001101</td><td>M</td><td>&amp;#77;</td><td>&nbsp;</td><td>Uppercase M</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 78"><i class="icon-plus-square"></i></button></td><td><a href="/78" title="ASCII Code 78">78</a></td><td>116</td><td>4E</td><td>01001110</td><td>N</td><td>&amp;#78;</td><td>&nbsp;</td><td>Uppercase N</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 79"><i class="icon-plus-square"></i></button></td><td><a href="/79" title="ASCII Code 79">79</a></td><td>117</td><td>4F</td><td>01001111</td><td>O</td><td>&amp;#79;</td><td>&nbsp;</td><td>Uppercase O</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 80"><i class="icon-plus-square"></i></button></td><td><a href="/80" title="ASCII Code 80">80</a></td><td>120</td><td>50</td><td>01010000</td><td>P</td><td>&amp;#80;</td><td>&nbsp;</td><td>Uppercase P</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 81"><i class="icon-plus-square"></i></button></td><td><a href="/81" title="ASCII Code 81">81</a></td><td>121</td><td>51</td><td>01010001</td><td>Q</td><td>&amp;#81;</td><td>&nbsp;</td><td>Uppercase Q</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 82"><i class="icon-plus-square"></i></button></td><td><a href="/82" title="ASCII Code 82">82</a></td><td>122</td><td>52</td><td>01010010</td><td>R</td><td>&amp;#82;</td><td>&nbsp;</td><td>Uppercase R</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 83"><i class="icon-plus-square"></i></button></td><td><a href="/83" title="ASCII Code 83">83</a></td><td>123</td><td>53</td><td>01010011</td><td>S</td><td>&amp;#83;</td><td>&nbsp;</td><td>Uppercase S</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 84"><i class="icon-plus-square"></i></button></td><td><a href="/84" title="ASCII Code 84">84</a></td><td>124</td><td>54</td><td>01010100</td><td>T</td><td>&amp;#84;</td><td>&nbsp;</td><td>Uppercase T</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 85"><i class="icon-plus-square"></i></button></td><td><a href="/85" title="ASCII Code 85">85</a></td><td>125</td><td>55</td><td>01010101</td><td>U</td><td>&amp;#85;</td><td>&nbsp;</td><td>Uppercase U</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 86"><i class="icon-plus-square"></i></button></td><td><a href="/86" title="ASCII Code 86">86</a></td><td>126</td><td>56</td><td>01010110</td><td>V</td><td>&amp;#86;</td><td>&nbsp;</td><td>Uppercase V</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 87"><i class="icon-plus-square"></i></button></td><td><a href="/87" title="ASCII Code 87">87</a></td><td>127</td><td>57</td><td>01010111</td><td>W</td><td>&amp;#87;</td><td>&nbsp;</td><td>Uppercase W</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 88"><i class="icon-plus-square"></i></button></td><td><a href="/88" title="ASCII Code 88">88</a></td><td>130</td><td>58</td><td>01011000</td><td>X</td><td>&amp;#88;</td><td>&nbsp;</td><td>Uppercase X</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 89"><i class="icon-plus-square"></i></button></td><td><a href="/89" title="ASCII Code 89">89</a></td><td>131</td><td>59</td><td>01011001</td><td>Y</td><td>&amp;#89;</td><td>&nbsp;</td><td>Uppercase Y</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 90"><i class="icon-plus-square"></i></button></td><td><a href="/90" title="ASCII Code 90">90</a></td><td>132</td><td>5A</td><td>01011010</td><td>Z</td><td>&amp;#90;</td><td>&nbsp;</td><td>Uppercase Z</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 91"><i class="icon-plus-square"></i></button></td><td><a href="/91" title="ASCII Code 91">91</a></td><td>133</td><td>5B</td><td>01011011</td><td>[</td><td>&amp;#91;</td><td>&amp;lsqb;</td><td>Opening bracket</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 92"><i class="icon-plus-square"></i></button></td><td><a href="/92" title="ASCII Code 92">92</a></td><td>134</td><td>5C</td><td>01011100</td><td>\</td><td>&amp;#92;</td><td>&amp;bsol;</td><td>Backslash</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 93"><i class="icon-plus-square"></i></button></td><td><a href="/93" title="ASCII Code 93">93</a></td><td>135</td><td>5D</td><td>01011101</td><td>]</td><td>&amp;#93;</td><td>&amp;rsqb;</td><td>Closing bracket</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 94"><i class="icon-plus-square"></i></button></td><td><a href="/94" title="ASCII Code 94">94</a></td><td>136</td><td>5E</td><td>01011110</td><td>^</td><td>&amp;#94;</td><td>&amp;Hat;</td><td>Caret - circumflex</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 95"><i class="icon-plus-square"></i></button></td><td><a href="/95" title="ASCII Code 95">95</a></td><td>137</td><td>5F</td><td>01011111</td><td>_</td><td>&amp;#95;</td><td>&amp;lowbar;</td><td>Underscore</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 96"><i class="icon-plus-square"></i></button></td><td><a href="/96" title="ASCII Code 96">96</a></td><td>140</td><td>60</td><td>01100000</td><td>`</td><td>&amp;#96;</td><td>&amp;grave;</td><td>Grave accent</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 97"><i class="icon-plus-square"></i></button></td><td><a href="/97" title="ASCII Code 97">97</a></td><td>141</td><td>61</td><td>01100001</td><td>a</td><td>&amp;#97;</td><td>&nbsp;</td><td>Lowercase a</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 98"><i class="icon-plus-square"></i></button></td><td><a href="/98" title="ASCII Code 98">98</a></td><td>142</td><td>62</td><td>01100010</td><td>b</td><td>&amp;#98;</td><td>&nbsp;</td><td>Lowercase b</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 99"><i class="icon-plus-square"></i></button></td><td><a href="/99" title="ASCII Code 99">99</a></td><td>143</td><td>63</td><td>01100011</td><td>c</td><td>&amp;#99;</td><td>&nbsp;</td><td>Lowercase c</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 100"><i class="icon-plus-square"></i></button></td><td><a href="/100" title="ASCII Code 100">100</a></td><td>144</td><td>64</td><td>01100100</td><td>d</td><td>&amp;#100;</td><td>&nbsp;</td><td>Lowercase d</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 101"><i class="icon-plus-square"></i></button></td><td><a href="/101" title="ASCII Code 101">101</a></td><td>145</td><td>65</td><td>01100101</td><td>e</td><td>&amp;#101;</td><td>&nbsp;</td><td>Lowercase e</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 102"><i class="icon-plus-square"></i></button></td><td><a href="/102" title="ASCII Code 102">102</a></td><td>146</td><td>66</td><td>01100110</td><td>f</td><td>&amp;#102;</td><td>&nbsp;</td><td>Lowercase f</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 103"><i class="icon-plus-square"></i></button></td><td><a href="/103" title="ASCII Code 103">103</a></td><td>147</td><td>67</td><td>01100111</td><td>g</td><td>&amp;#103;</td><td>&nbsp;</td><td>Lowercase g</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 104"><i class="icon-plus-square"></i></button></td><td><a href="/104" title="ASCII Code 104">104</a></td><td>150</td><td>68</td><td>01101000</td><td>h</td><td>&amp;#104;</td><td>&nbsp;</td><td>Lowercase h</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 105"><i class="icon-plus-square"></i></button></td><td><a href="/105" title="ASCII Code 105">105</a></td><td>151</td><td>69</td><td>01101001</td><td>i</td><td>&amp;#105;</td><td>&nbsp;</td><td>Lowercase i</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 106"><i class="icon-plus-square"></i></button></td><td><a href="/106" title="ASCII Code 106">106</a></td><td>152</td><td>6A</td><td>01101010</td><td>j</td><td>&amp;#106;</td><td>&nbsp;</td><td>Lowercase j</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 107"><i class="icon-plus-square"></i></button></td><td><a href="/107" title="ASCII Code 107">107</a></td><td>153</td><td>6B</td><td>01101011</td><td>k</td><td>&amp;#107;</td><td>&nbsp;</td><td>Lowercase k</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 108"><i class="icon-plus-square"></i></button></td><td><a href="/108" title="ASCII Code 108">108</a></td><td>154</td><td>6C</td><td>01101100</td><td>l</td><td>&amp;#108;</td><td>&nbsp;</td><td>Lowercase l</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 109"><i class="icon-plus-square"></i></button></td><td><a href="/109" title="ASCII Code 109">109</a></td><td>155</td><td>6D</td><td>01101101</td><td>m</td><td>&amp;#109;</td><td>&nbsp;</td><td>Lowercase m</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 110"><i class="icon-plus-square"></i></button></td><td><a href="/110" title="ASCII Code 110">110</a></td><td>156</td><td>6E</td><td>01101110</td><td>n</td><td>&amp;#110;</td><td>&nbsp;</td><td>Lowercase n</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 111"><i class="icon-plus-square"></i></button></td><td><a href="/111" title="ASCII Code 111">111</a></td><td>157</td><td>6F</td><td>01101111</td><td>o</td><td>&amp;#111;</td><td>&nbsp;</td><td>Lowercase o</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 112"><i class="icon-plus-square"></i></button></td><td><a href="/112" title="ASCII Code 112">112</a></td><td>160</td><td>70</td><td>01110000</td><td>p</td><td>&amp;#112;</td><td>&nbsp;</td><td>Lowercase p</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 113"><i class="icon-plus-square"></i></button></td><td><a href="/113" title="ASCII Code 113">113</a></td><td>161</td><td>71</td><td>01110001</td><td>q</td><td>&amp;#113;</td><td>&nbsp;</td><td>Lowercase q</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 114"><i class="icon-plus-square"></i></button></td><td><a href="/114" title="ASCII Code 114">114</a></td><td>162</td><td>72</td><td>01110010</td><td>r</td><td>&amp;#114;</td><td>&nbsp;</td><td>Lowercase r</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 115"><i class="icon-plus-square"></i></button></td><td><a href="/115" title="ASCII Code 115">115</a></td><td>163</td><td>73</td><td>01110011</td><td>s</td><td>&amp;#115;</td><td>&nbsp;</td><td>Lowercase s</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 116"><i class="icon-plus-square"></i></button></td><td><a href="/116" title="ASCII Code 116">116</a></td><td>164</td><td>74</td><td>01110100</td><td>t</td><td>&amp;#116;</td><td>&nbsp;</td><td>Lowercase t</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 117"><i class="icon-plus-square"></i></button></td><td><a href="/117" title="ASCII Code 117">117</a></td><td>165</td><td>75</td><td>01110101</td><td>u</td><td>&amp;#117;</td><td>&nbsp;</td><td>Lowercase u</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 118"><i class="icon-plus-square"></i></button></td><td><a href="/118" title="ASCII Code 118">118</a></td><td>166</td><td>76</td><td>01110110</td><td>v</td><td>&amp;#118;</td><td>&nbsp;</td><td>Lowercase v</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 119"><i class="icon-plus-square"></i></button></td><td><a href="/119" title="ASCII Code 119">119</a></td><td>167</td><td>77</td><td>01110111</td><td>w</td><td>&amp;#119;</td><td>&nbsp;</td><td>Lowercase w</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 120"><i class="icon-plus-square"></i></button></td><td><a href="/120" title="ASCII Code 120">120</a></td><td>170</td><td>78</td><td>01111000</td><td>x</td><td>&amp;#120;</td><td>&nbsp;</td><td>Lowercase x</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 121"><i class="icon-plus-square"></i></button></td><td><a href="/121" title="ASCII Code 121">121</a></td><td>171</td><td>79</td><td>01111001</td><td>y</td><td>&amp;#121;</td><td>&nbsp;</td><td>Lowercase y</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 122"><i class="icon-plus-square"></i></button></td><td><a href="/122" title="ASCII Code 122">122</a></td><td>172</td><td>7A</td><td>01111010</td><td>z</td><td>&amp;#122;</td><td>&nbsp;</td><td>Lowercase z</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 123"><i class="icon-plus-square"></i></button></td><td><a href="/123" title="ASCII Code 123">123</a></td><td>173</td><td>7B</td><td>01111011</td><td>{</td><td>&amp;#123;</td><td>&amp;lcub;</td><td>Opening brace</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 124"><i class="icon-plus-square"></i></button></td><td><a href="/124" title="ASCII Code 124">124</a></td><td>174</td><td>7C</td><td>01111100</td><td>|</td><td>&amp;#124;</td><td>&amp;verbar;</td><td>Vertical bar</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 125"><i class="icon-plus-square"></i></button></td><td><a href="/125" title="ASCII Code 125">125</a></td><td>175</td><td>7D</td><td>01111101</td><td>}</td><td>&amp;#125;</td><td>&amp;rcub;</td><td>Closing brace</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 126"><i class="icon-plus-square"></i></button></td><td><a href="/126" title="ASCII Code 126">126</a></td><td>176</td><td>7E</td><td>01111110</td><td>~</td><td>&amp;#126;</td><td>&amp;tilde;</td><td>Equivalency sign - tilde</td></tr><tr><td><button class="btn-index text-primary" title="Show more about code 127"><i class="icon-plus-square"></i></button></td><td><a href="/127" title="ASCII Code 127">127</a></td><td>177</td><td>7F</td><td>01111111</td><td>DEL</td><td>&amp;#127;</td><td>&nbsp;</td><td>Delete</td></tr>            </tbody>
</table>

# LAB - LED display

You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) – that's how we imagine it:
```cmd
  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
```
Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.
