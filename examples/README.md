# Examples

This directory includes a number of working examples of Acme agents. These
examples are not meant to be comprehensive and instead show a number of common
use cases under which Acme agents can be applied.

Our [quickstart] can be used to get running quickly. This
notebook will show how to instantiate a simple agent and run it on an
environment. You can also take a look at our [tutorial], which takes a more
in-depth look at the construction of the D4PG agent. This also highlights the
general structure of most Acme agents which applies more broadly to all agents
implemented in Acme.

[quickstart]: /../../blob/master/examples/quickstart.ipynb
[tutorial]: /../../blob/master/examples/tutorial.ipynb


## Continuous control

We include a number of agents running on continuous control tasks. These agents
are representative examples, but any continuous control algorithm implemented in
Acme should be able to be swapped in.

Note that many of the examples, particularly those based on the DeepMind Control
Suite, will require a [MuJoCo license](https://www.roboti.us/license.html) in
order to run. See our [tutorial] for more details or see refer to the
[dm_control] repository for further information.

-   [D4PG](control/run_d4pg.py): a deterministic policy gradient (D4PG) agent
    which includes a determinstic policy and a distributional critic running on
    the DeepMind Control Suite.
-   [D4PG (gym)](control/run_d4pg_gym.py): this example runs the same algorithm
    on a number of tasks defined in the [OpenAI Gym]. By default this will run
    the "mountain car" domain which does not require a MuJoCo license.
-   [DMPO](control/run_dmpo.py): a maximum-a-posterior policy optimization
    agent which combines both a distributional critic and a stochastic policy.

[dm_control]: https://github.com/deepmind/dm_control
[OpenAI Gym]: https://github.com/openai/gym


## Discrete agents (Atari)

The development of the [Arcade Learning environment] and the coinciding use
of Atari as a benchmark has played a very prominent role in the modern usage and
testing of reinforcement learning algorithms. As a result we've also included
direct examples of prominent discrete-action algorithms implemented in Acme and
running on this environment.

-   [DQN](/../../blob/master/examples/atari/run_dqn.py): a "classic" benchmark agent for Atari; and
-   [R2D2](/../../blob/master/examples/atari/run_r2d2.py): a more recent Q-learning variant which includes
    recurrence.

[Arcade Learning environment]: https://arxiv.org/abs/1207.4708


## Offline agents

Acme includes examples of offline agents, i.e. agents trained using external
data generated by another agent:

-   [BC](/../../blob/master/examples/offline/run_bc.py): a behaviour cloning agent.
-   [BC (JAX)](/../../blob/master/examples/offline/run_bc_jax.py): a behaviour cloning agent (implemented
    in jax).
-   [BCQ](/../../blob/master/examples/offline/run_bcq.py): an implementation of BCQ.

Similarly we also include so-called "from demonstration" agents which mix
offline and online data:

-   [DQfD](/../../blob/master/examples/offline/run_dqfd.py): the DQfD agent running on hard-exploration
    tasks within bsuite (e.g. deep sea) using demonstration data; and


## Behaviour Suite

The [Behaviour Suite for Reinforcement Learning](bsuite) defines a collection
of tasks and environments which collectively investigate core capabilities of RL
algorithms across a number of different axes. The examples we include
show how to run Acme agents on this suite.

-   [DQN](/../../blob/master/examples/bsuite/run_dqn.py): an off-policy DQN examples;
-   [Impala](/../../blob/master/examples/bsuite/run_impala.py): an on-policy Impala agent; and
-   [MCTS](/../../blob/master/examples/bsuite/run_mcts.py): a model-based agent running on the
    task suite using either a simulator of the environment or a learned model.

For more information see https://github.com/deepmind/bsuite.

[bsuite]: https://github.com/deepmind/bsuite
