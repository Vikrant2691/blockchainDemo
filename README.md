# Simple Blockchain ERC20 token
Token name is SHB_10403


## Run via Docker

docker pull and run
```
docker run vison91/blockchain_demonstration
```
## Send tokens
```
curl command for token transfer
curl --header "Content-Type: application/json" --request POST --data '{"address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C"}' http://localhost:8080/token

curl command for eth transfer
curl --header "Content-Type: application/json" --request POST --data '{"address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C", "amount":"0.05"}' http://localhost:8080/eth

## basic curl check
```
curl http://localhost:8080/amiworking
```