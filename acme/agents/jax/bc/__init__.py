# python3
# Copyright 2018 DeepMind Technologies Limited. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Implementation of a behavior cloning (BC) agent."""

from acme.agents.jax.bc import pretraining
from acme.agents.jax.bc.learning import make_bc_learner_core
from acme.agents.jax.bc.learning import TrainingState
from acme.agents.jax.bc.losses import logp
from acme.agents.jax.bc.losses import Loss
from acme.agents.jax.bc.losses import mse
from acme.agents.jax.bc.losses import peerbc
from acme.agents.jax.bc.losses import rcal
