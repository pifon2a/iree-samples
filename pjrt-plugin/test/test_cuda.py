import jax
from jax._src.lib import xla_bridge
from jax._src.lib import xla_client

def iree_backend_factory():
  # Can also load in code:
  # xla_client._xla.load_pjrt_plugin("iree_cuda", "/path/to/plugin.so")
  return xla_client._xla.get_c_api_client("iree_cuda")

xla_bridge.register_backend_factory("iree_cuda", iree_backend_factory)

# actually this is a better way to make sure jax uses your plugin, it'll raise an error if it can't initialize
jax.config.update("jax_platforms", "iree_cuda")


print(jax.numpy.add(1, 1))
