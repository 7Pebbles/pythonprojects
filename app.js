const CharacterAI = require('node_characterai');
const characterAI = new CharacterAI();
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

(async() => {
    await characterAI.authenticateAsGuest();

    const characterId = "eP7G9I6yOj7hNwd_N1UQnc6DyK7tKnjqQ7dKasi2_d4" 

    const chat = await characterAI.createOrContinueChat(characterId);
    const response = await chat.sendAndAwaitResponse('Hello', true)
    for (let i = 0; i < 1000; i++) {
        const answer = await new Promise(resolve => {
          rl.question("\x1b[31mPrompt: \x1b[0m", resolve);
        });
        const response = await chat.sendAndAwaitResponse(answer, true);
        console.log('\x1b[34mAI: \x1b[0m' + response.text);
      }
      
 
})();
