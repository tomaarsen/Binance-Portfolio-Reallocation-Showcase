# Binance-Portfolio-Reallocation-Showcase
Some of us may have some long-term crypto holds. 
A common strategy for these coins is to buy a roughly equal amount of all of them, and just hold on for a long time.
This strategy isn't flawless, however. 
Let's assume you pick 5 coins, each 20% of your portfolio. 
If 4 of the 5 don't end up moving much, but one of them explodes 300%, then the value of your portfolio heavily depends on that one coin. It now represents a massive 43% of your portfolio, meaning that your attempts to diversify your portfolio will largely be undone.

Luckily, there's a method to help prevent this.

---

## Portfolio Reallocation
The concept of this method is simple. The value of your holdings should follow a specific, predetermined ratio. This ratio can be anything. If you have two coins, with a ratio of 1:1, and one of them goes up in value, the ratio will shift from 50% and 50% to for example 54% and 46%. A reallocation bot will then sell some of the coin that performed well, and invest it in the coin that didn't. The new percent will yet again be 50% and 50% (back to equal on both sides, 1:1).

That's the concept. If you take a moment to think about it, you realise that this bot will sell whenever a coin goes up, and buy whenever a coin goes down. This means the bot will automatically take profits from profitable coins, and reinvest this money in coins that performed poorly. This bot is essentially the definition of "Buy low, sell high".

<b>But</b>, what about transaction fees? Wouldn't they eat into your profits?<br>
And what if a coin just goes up a bunch, and the bot keeps selling parts for a coin that isn't moving at all? 
Wouldn't it be more profitable to just hold and not bother?

Great questions. I didn't know either.

So, to test it, I wrote a script to plot the performance of this bot, relative to just holding. The script by default picks out 3 Binance coins at random, uses as much historical data as is available, and plots the performance relative to just holding. It's possible to edit the amount of coins it randomly picks, by editing the `randomCoinAmount` variable, and it's possible to have the script look at the coins you want, by editing the `symbolList` variable.

It turns out, in a large amount of cases, it would have been more profitable to have this hypothetical bot active on the coins, instead of just holding the coins, even with fees.

---

## Requirements
- Python 3.6+ (Required for Pandas)<br>
- Requests Module<br>
- Matplotlib Module<br>
- Pandas Module

---

## Graph gallery
Disclaimer: The only graphs I did not include were graphs where one of the coins only had historical data for less than 100 entries. Beyond that I picked the 20 first graphs that got generated. The graphs include 3 coins, set at a ratio of 1:1:1. A bot could hypothetically have different ratios too, depending on what coins you're more bullish on. Consider focusing on the Blue and Yellow lines. Blue showcases the hypothetical bot performance, while yellow shows the performance of holding the coins without any trades. <br>
The [gallery](https://imgur.com/gallery/JSNaXpk).

The data from these 20 tests is as follows:<br>
<table>
  <tr>
    <th>ID</th>
    <th>Profit Ratio with Bot</th>
    <th>Profit Ratio without Bot</th>
    <th>Ratio between the Two</th>
  </tr>
  <tr>
    <td>1</td>
    <td><b>0.56</b></td>
    <td>0.54</td>
    <td><b>1.03</b></td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.61</td>
    <td><b>0.85</b></td>
    <td>0.72</td>
  </tr>
  <tr>
    <td>3</td>
    <td><b>0.80</b></td>
    <td>0.59</td>
    <td><b>1.36</b></td>
  </tr>
  <tr>
    <td>4</td>
    <td><b>1.75</b></td>
    <td>1.22</td>
    <td><b>1.43</b></td>
  </tr>
  <tr>
    <td>5</td>
    <td><b>1.77</b></td>
    <td>1.30</td>
    <td><b>1.36</b></td>
  </tr>
  <tr>
    <td>6</td>
    <td><b>3.33</b></td>
    <td>3.06</td>
    <td><b>1.08</b></td>
  </tr>
  <tr>
    <td>7</td>
    <td><b>2.91</b></td>
    <td>2.42</td>
    <td><b>1.20</b></td>
  </tr>
  <tr>
    <td>8</td>
    <td><b>2.99</b></td>
    <td>2.76</td>
    <td><b>1.08</b></td>
  </tr>
  <tr>
    <td>9</td>
    <td><b>0.61</b></td>
    <td>0.58</td>
    <td><b>1.05</b></td>
  </tr>
  <tr>
    <td>10</td>
    <td><b>0.83</b></td>
    <td>0.69</td>
    <td><b>1.20</b></td>
  </tr>
  <tr>
    <td>11</td>
    <td><b>2.41</b></td>
    <td>1.94</td>
    <td><b>1.24</b></td>
  </tr>
  <tr>
    <td>12</td>
    <td><b>0.73</b></td>
    <td>0.71</td>
    <td><b>1.03</b></td>
  </tr>
  <tr>
    <td>13</td>
    <td>0.70</td>
    <td><b>0.70</b></td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>14</td>
    <td><b>0.72</b></td>
    <td>0.57</td>
    <td><b>1.26</b></td>
  </tr>
  <tr>
    <td>15</td>
    <td>0.54</td>
    <td><b>0.68</b></td>
    <td>0.79</td>
  </tr>
  <tr>
    <td>16</td>
    <td>10.05</td>
    <td><b>12.29</b></td>
    <td>0.82</td>
  </tr>
  <tr>
    <td>17</td>
    <td><b>0.51</b></td>
    <td>0.42</td>
    <td><b>1.21</b></td>
  </tr>
  <tr>
    <td>18</td>
    <td><b>0.79</b></td>
    <td>0.52</td>
    <td><b>1.52</b></td>
  </tr>
  <tr>
    <td>19</td>
    <td><b>0.49</b></td>
    <td>0.45</td>
    <td><b>1.09</b></td>
  </tr>
  <tr>
    <td>20</td>
    <td><b>1.04</b></td>
    <td>0.76</td>
    <td><b>1.37</b></td>
  </tr>
  <tr>
    <td><b>Average</b></td>
    <td>-</td>
    <td>-</td>
    <td><b>1.142</b></td>
  </tr>
</table>
