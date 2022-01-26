# How to get historical transactions on Polygon? 

Ethereum Layer 2 scaling solutions, like Polygon, have allowed developers to take advantage of low transaction costs and far faster confirmation times. However, this introduces a new challenge for devs: how to process and store large swaths of blockchain data. Traditionally, developers had to spin up, manage, and index across their own nodes to build databases. This left developers constrained by an expensive and slow solution that ultimately limits their apps’ feature sets regardless of whether they are deployed on Layer 1 or Layer 2 solutions.

While building historical queries into dApps has traditionally been complicated and time-consuming, the Alchemy Transfers API on Polygon allows for developers to get Polygon transaction details, dating back to the very beginning, in a single request. 

In this tutorial, we’ll look at an example of how, with just a few lines of code, your Polygon dApp can integrate historical transactions. 

## Understanding Alchemy Transfers API on Polygon

In this example, we are trying to query and find the transfer of [this transaction](https://polygonscan.com/tx/0x1e85ace98f4fc4ad7b1b64465df81d0a275d494421e553e23a238b156f42b17f). We can see from Polyscan that ~12,000 USDT was transferred from [0x5350e1068f0e138ff306990b16fa4910d970c692](https://polygonscan.com/token/0xc2132d05d31c914a87c6611c10748aeb04b58e8f?a=0x5350e1068f0e138ff306990b16fa4910d970c692) to [0x9d2b758e3ffd2569c6956676fae7f8b71a53ffb5](https://www.google.com/url?q=https://polygonscan.com/token/0xc2132d05d31c914a87c6611c10748aeb04b58e8f?a%3D0x9d2b758e3ffd2569c6956676fae7f8b71a53ffb5&sa=D&source=docs&ust=1643161531590007&usg=AOvVaw3vJ842uYyQ1Hqqjsp03eXy).

