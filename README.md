# StupidYugiohRelatedScripts
Run

```
curl https://db.ygoprodeck.com/api/v7/cardinfo.php >> yugiohcarddatabasedump
```

in the directory you want to run the script to get a dump of all yugioh cards in the format these scripts assume.

Any useful output will be to stdout. Use pipes if you want it to output to files.

Example usage (from the directory you cloned this repo into):

```
curl https://db.ygoprodeck.com/api/v7/cardinfo.php >> yugiohcarddatabasedump # Only do this the first time
./generaterandomdeck.py > random.ydk
```

