const { Contract, Account, invoke, getContract } = require('@arcblock/forge-sdk');

async function main() {
  const owner = '0x2a2db9eb27052b828169cf9bb6c040ddb60d5230651ec16ce916b9eeae8d22a1';
  const network = 'http://34.159.107.195:18545/951446a4-9daa-427b-a755-0a5911f467c5';

  const setupAddress = '0xc2C58254C6BCe019C962B3C077621DA27C9Fbf61';
  const setupContract = getContract(setupAddress, 'Setup');

  // Check the challenge status
  const isSolved = await invoke({
    method: 'isSolved',
    params: [],
    contract: setupContract,
    sender: owner,
    network,
  });

  console.log('Is Challenge Solved?', isSolved);
}

main();
