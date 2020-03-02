# Background and Literature Review

## Potential problems we could solve

### The stop button problem

A very interesting problem based on how to deal with having a manual stop button on a superintelligent agent that might learn to fight you and stop you from hitting the stop button. Trying to align our interests exactly with the agent's interests is a pretty complex problem and this might be too complex for us to solve right now but it's worth exploring a bit. Here are some interesting resources regarding this problem:

* https://www.youtube.com/watch?v=3TYT1QfdfsM&t=2s
* https://www.youtube.com/watch?v=9nktr1MgS-A
* https://arxiv.org/pdf/1606.03137.pdf

### Learning to play Atari games

Using OpenAI Gym, we can simulate an Atari game. Our Agent will only have the frames and reward as the observation. We could also train multiple models and make them play against each other to see which performs better against others. The game would have to support inputs from 2 agents though. A simple example for a environment is in (/examples/boxing_sim.py)[../examples/boxing_sim.py]
