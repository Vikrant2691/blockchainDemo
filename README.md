# Simple Blockchain ERC20 token
Token name is SHB_10403

## Description of service
The python web service can be used to transfer tokens to an account provided by the user through Rest API calls.

Data packet format:
To transfer ethereum tokens http://0.0.0.0:8081/eth
```
data {
    "address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C"
    }
```
To transfer custom tokens creted by the contract http://0.0.0.0:8081/token
```
data {
    "address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C",
    "amount":"0.05"
    }

if the balance of target account is greated than 1000, then 1 token will be transfered. Otherwise 1000 token will be transfered
```

## Smart Contract creation:
The smart contract is created using '''ERC20.sol file'''
This contract can be used by different parties to transfer funds in token amount. 

## Transfer of funds:
The contract of this token in mentioned the .env file
```
CONTRACT_ADDRESS=0xaa940d07cd978f953863c80da92e544b1c22195b <-- The contract-id for SHB_10403
OWNER_ADDRESS=0x51E8A0b42A79e9CeaA12DBe6C336D8f04B079271 <-- Sender's account id
SUPER_SECRET_PRIVATE_KEY= <super secret private key of the account holder>
```
## Send tokens
Basic curl check
```
curl http://localhost:8080/amiworking
```
Send tokens
```
curl command for token transfer
curl --header "Content-Type: application/json" --request POST --data '{"address":"0x972e91330E79b111e1eFB878009Bd851339526Cd"}' http://localhost:8080/token
```
Send eth
```
curl command for eth transfer
curl --header "Content-Type: application/json" --request POST --data '{"address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C", "amount":"0.05"}' http://localhost:8080/eth
```

## Run via Docker


```
 docker compose up
```
