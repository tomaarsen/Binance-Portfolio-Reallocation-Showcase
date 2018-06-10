# Binance-Portfolio-Reallocation-Showcase
Many of us likely have some long-term crypto holds. 
A common strategy for these coins is to buy a roughly equal amount of all of them, and just hold on for a long time.
This strategy isn't flawless, however. 
Let's assume you pick 5 coins, each 20% of your portfolio. 
If 4 of the 5 don't end up moving much, but one of them explodes 300%, then the value of your portfolio heavily depends on that one coin.
If that coin crashes, you lose a lot. <br><br>
Luckily, there's a method to help prevent this. <br>

<b>Portfolio Reallocation</b><br>
The concept of this method is simple. The value of your holdings should follow a specific, predetermined ratio. 
This ratio can be anything. 
If you have two coins, with a ratio of 1:1, and one of them goes up in value, the ratio will shift from 50% and 50% to for example
54% and 46%. A reallocation bot will then sell some of the coin that performed well, and invest it in the coin that didn't. 
The new percent will yet again be 50% and 50% (back to equal on both sides, 1:1).<br>

That's the concept. If you think about it properly, you realise that this bot will sell whenever a coin goes up, and buy whenever a coin goes down.
This means the bot will automatically take profits of profitable coins, and reinvest lower for coins that performed poorly.
This coin is essentially the definition of "Buy low sell high".<br>

<b>But</b>, what about fees? Wouldn't they eat into your profits?<br>
And what if a coin just goes up a bunch, and the bot keeps selling parts for a coin that isn't moving at all? 
Wouldn't that be less profitable than just holding?<br><br>
Great questions. I didn't know either. <br><br>
So, to test it, I wrote a script to plot the performance of this bot, relative to just holding. 
The script by default picks out 3 Binance coins at random, uses as much historical data as is available, and plots the performance relative to just holding.
It's possible to edit the amount of coins it randomly picks, by editing the `randomCoinAmount` variable, and it's possible to have the script look at the coins you want,
by editing the `symbolList` variable.<br>
It turns out, in a large amount of cases, it would have been more profitable to hold coins with this bot active, than just holding the coins, even with fees.
<br><br>
<b>Requirements</b><br>
-Python 3.6+ (Required for Pandas)<br>
-Requests Module<br>
-Matplotlib Module<br>
-Pandas Module<br>
<br>
<b>Graph gallery</b><br>
Disclaimer: The only graphs I did not include were graphs where one of the coins only had historical data for <100 entries. Beyond that I picked the 20 first graphs that got generated.<br>
The graphs include 3 coins, set at a ratio of 1:1:1. A bot could hypothetically have different ratios too, depending on what coins you're more bullish on.<br>
Consider focusing on the Blue and Yellow lines. Blue showcases the hypothetical bot performance, while yellow shows the performance of holding the coins without any trades. <br>
https://imgur.com/gallery/JSNaXpk<br>

The data from these 20 tests is as follows:<br>
<table>
  <tr>
    <th>ID</th>
    <th>Profit Ratio with Bot</th>
    <th>Profit Ratio without Bot</th>
  </tr>
  <tr>
    <td>1</td>
    <td><b>0.56x</b></td>
    <td>0.54x</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.61x</td>
    <td><b>0.85x</b></td>
  </tr>
  <tr>
    <td>3</td>
    <td><b>0.80x</b></td>
    <td>0.59x</td>
  </tr>
  <tr>
    <td>4</td>
    <td><b>1.75x</b></td>
    <td>1.22x</td>
  </tr>
  <tr>
    <td>5</td>
    <td><b>1.77x</b></td>
    <td>1.30x</td>
  </tr>
  <tr>
    <td>6</td>
    <td><b>3.33x</b></td>
    <td>3.06x</td>
  </tr>
  <tr>
    <td>7</td>
    <td><b>2.91x</b></td>
    <td>2.42x</td>
  </tr>
  <tr>
    <td>8</td>
    <td><b>2.99x</b></td>
    <td>2.76x</td>
  </tr>
  <tr>
    <td>9</td>
    <td><b>0.61x</b></td>
    <td>0.58x</td>
  </tr>
  <tr>
    <td>10</td>
    <td><b>0.83x</b></td>
    <td>0.69x</td>
  </tr>
  <tr>
    <td>11</td>
    <td><b>2.41x</b></td>
    <td>1.94x</td>
  </tr>
  <tr>
    <td>12</td>
    <td><b>0.73x</b></td>
    <td>0.71x</td>
  </tr>
  <tr>
    <td>13</td>
    <td>0.70x</td>
    <td><b>0.70x</b></td>
  </tr>
  <tr>
    <td>14</td>
    <td><b>0.72x</b></td>
    <td>0.57x</td>
  </tr>
  <tr>
    <td>15</td>
    <td>0.54x</td>
    <td><b>0.68x</b></td>
  </tr>
  <tr>
    <td>16</td>
    <td>10.05x</td>
    <td><b>12.29x</b></td>
  </tr>
  <tr>
    <td>17</td>
    <td><b>0.51x</b></td>
    <td>0.42x</td>
  </tr>
  <tr>
    <td>18</td>
    <td><b>0.79x</b></td>
    <td>0.52x</td>
  </tr>
  <tr>
    <td>19</td>
    <td><b>0.49x</b></td>
    <td>0.45x</td>
  </tr>
  <tr>
    <td>20</td>
    <td><b>1.04x</b></td>
    <td>0.76x</td>
  </tr>
</table>
