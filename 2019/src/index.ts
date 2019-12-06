const day = process.argv[2];

// tslint:disable-next-line:no-var-requires
const {part1, part2} = require(`./${day}`);

console.log(`${day} part1 >`, part1(`${__dirname}/${day}/input.txt`));
console.log(`${day} part2 >`, part2(`${__dirname}/${day}/input.txt`));

