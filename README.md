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
If you have two coins, with a ratio of 50:50 (a 1:1 ratio), and one of them goes up in value, the ratio will shift to for example
54:50. A reallocation bot will then sell some of the coin that performed well, and invest it in the coin that didn't. 
The new ratio will be 52:52 (back to 1:1).<br>

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
-Python 3+<br>
-Requests Module<br>
-Matplotlib Module<br>
-Pandas Module<br>
<br>
<b>Graph gallery yet to come</b>
