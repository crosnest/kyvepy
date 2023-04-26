# Install kyved
git clone https://github.com/chain4energy/kyve-chain
cd kyve-chain
git checkout v1.2.0
make install

# Remove kyved git folder
cd .. && rm -rf kyve-chain


# Add symlink of kyved
sudo ln -s ~/go/bin/ce4ed /usr/local/bin/kyved

# Export PATH
if [[ "$OSTYPE" == "darwin"* ]]; then
  export GOPATH=$HOME/go
  export PATH=$GOPATH/bin:$PATH
fi

# Clear the existing configuration
rm -rf ~/.kyved*

# Add keys
echo "erase weekend bid boss knee vintage goat syrup use tumble device album fortune water sweet maple kind degree toss owner crane half useless sleep" |kyved keys add validator --recover

echo "account snack twist chef razor sing gain birth check identify unable vendor model utility fragile stadium turtle sun sail enemy violin either keep fiction" | kyved keys add bob --recover

# Start kyved local node

# Configure node
kyved init --chain-id=testing testing
kyved add-genesis-account $(kyved keys show validator -a) 100000000000000000000000stake
kyved add-genesis-account $(kyved keys show bob -a) 100000000ukyve
kyved gentx validator 10000000000000000000000stake --chain-id testing
kyved collect-gentxs

# Enable rest-api
sed -i '/^\[api\]$/,/^\[/ s/^enable = false/enable = true/' ~/.kyved/config/app.toml
