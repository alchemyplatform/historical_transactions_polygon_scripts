# How to get historical transactions on Polygon? 

Ethereum Layer 2 scaling solutions, like Polygon, have allowed developers to take advantage of low transaction costs and far faster confirmation times. However, this introduces a new challenge for devs: how to process and store large swaths of blockchain data. Traditionally, developers had to spin up, manage, and index across their own nodes to build databases. This left developers constrained by an expensive and slow solution that ultimately limits their apps’ feature sets regardless of whether they are deployed on Layer 1 or Layer 2 solutions.

While building historical queries into dApps has traditionally been complicated and time-consuming, the Alchemy Transfers API on Polygon allows for developers to get Polygon transaction details, dating back to the very beginning, in a single request. 

In this tutorial, we’ll look at an example of how, with just a few lines of code, your Polygon dApp can integrate historical transactions. 

## Understanding Alchemy Transfers API on Polygon

In this example, we are trying to query and find the transfer of [this transaction](https://polygonscan.com/tx/0x1e85ace98f4fc4ad7b1b64465df81d0a275d494421e553e23a238b156f42b17f). We can see from Polyscan that ~12,000 USDT was transferred from [0x5350e1068f0e138ff306990b16fa4910d970c692](https://polygonscan.com/token/0xc2132d05d31c914a87c6611c10748aeb04b58e8f?a=0x5350e1068f0e138ff306990b16fa4910d970c692) to [0x9d2b758e3ffd2569c6956676fae7f8b71a53ffb5](https://www.google.com/url?q=https://polygonscan.com/token/0xc2132d05d31c914a87c6611c10748aeb04b58e8f?a%3D0x9d2b758e3ffd2569c6956676fae7f8b71a53ffb5&sa=D&source=docs&ust=1643161531590007&usg=AOvVaw3vJ842uYyQ1Hqqjsp03eXy).

To use the Transfers API to track the USDT transfer, we need a few pieces of key information that help narrow down our search. We format this request information into a JSON object as follows:

```
{
   "jsonrpc":"2.0",
   "id":0,
   "method":"alchemy_getAssetTransfers",
   "params":[
      {
         "fromBlock":"from_Block",
         "toBlock":"to_Block",
         "fromAddress":"FROM_ADDRESS",
         "toAddress":"TO_ADDRESS",
         "contractAddresses":[
            "USDT_ADDRESS"
         ],
         "category":[
            "erc20"
         ]
      }
   ]
})
```

## 1. From Block & To Block

We can reduce the amount of time it takes for the API to return our JSON response by constraining the start and end block numbers that we are attempting to search. 

Our transaction takes place in block 23876472 so we adjust our search to a small buffer around this block number. 

>The JSON object allows us to either use a hexadecimal string or for block number inputs. In this case, we use hexadecimals, so we input *0x16C5376* for a `fromBlock` of 23876470 and *0x16C537A* for a `toBlock` of 23876474)

## 2. To & From Addresses 

The To & From addresses represent where the transaction was sent and where it originated from respectively. In our example, To Address is 0x9d2b758e3ffd2569c6956676fae7f8b71a53ffb5 and From Address is 0x5350e1068f0e138ff306990b16fa4910d970c692.

## 3. Contract Address

The contract address is the address denoting the specific ERC20, ERC721, or ERC1155 contract that we seek to find.  In our example, the ERC20 contract for Polygon USDT is 0xc2132d05d31c914a87c6611c10748aeb04b58e8f. 

>Putting together this information, we can now use Alchemy’s Composer tool to return results that include our target transaction. [Visit this Alchemy Composer Example!](https://composer.alchemyapi.io?composer_state=%7B%22chain%22%3A2%2C%22network%22%3A401%2C%22methodName%22%3A%22alchemy_getAssetTransfers%22%2C%22paramValues%22%3A%5B%7B%22excludeZeroValue%22%3Atrue%2C%22fromBlock%22%3A%220x16C5376%22%2C%22toAddress%22%3A%220x9d2b758e3ffd2569c6956676fae7f8b71a53ffb5%22%2C%22contractAddresses%22%3A%22%5B%5C%220xc2132d05d31c914a87c6611c10748aeb04b58e8f%5C%22%5D%22%2C%22fromAddress%22%3A%220x5350e1068f0e138ff306990b16fa4910d970c692%22%2C%22category%22%3A%5B%22erc20%22%5D%2C%22toBlock%22%3A%220x16C537A%22%7D%5D%7D)

## To use this starter script, insert your Alchemy Key for API access:

>If you don’t already have one, you’ll first need to create an account on Alchemy. The free version will work fine for getting started!

Replace the string “ALCHEMY KEY” with your own private API key in `main.py`. 

```
ALCHEMY_KEY = “ALCHEMY KEY”
w3 = Web3(Web3.HTTPProvider('https://polygon-mainnet.alchemyapi.io/v2/'+ALCHEMY_KEY))
```

Run the `main.py` python script and confirm that your command line output returns the following:

![command_line_output](https://i.postimg.cc/ZR1HLRNX/Screen-Shot-2022-01-18-at-5-20-53-PM.png)

