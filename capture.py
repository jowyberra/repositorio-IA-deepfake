import torch
import numpy as np
import tensorflow as tf

def tensor_to_numpy(tensor):
    """
    Convert a PyTorch tensor to a NumPy array.
    """
    return tensor.cpu().numpy()

def numpy_to_tensor(array):
    """
    Convert a NumPy array to a PyTorch tensor.
    """
    return torch.from_numpy(array)

def tensor_to_tf(tensor):
    """
    Convert a PyTorch tensor to a TensorFlow tensor.
    """
    return tf.convert_to_tensor(tensor.cpu().numpy())

def tf_to_tensor(tf_tensor):
    """
    Convert a TensorFlow tensor to a PyTorch tensor.
    """
    return torch.from_numpy(tf_tensor.numpy())

def numpy_to_tf(array):
    """
    Convert a NumPy array to a TensorFlow tensor.
    """
    return tf.convert_to_tensor(array)

def tf_to_numpy(tf_tensor):
    """
    Convert a TensorFlow tensor to a NumPy array.
    """
    return tf_tensor.numpy()

# Debugging utilities
def print_tensor_info(tensor, name="Tensor"):
    """
    Print information about a PyTorch tensor.
    """
    print(f"{name}:")
    print(f"Shape: {tensor.shape}")
    print(f"Data type: {tensor.dtype}")
    print(f"Device: {tensor.device}")
    print(f"Values: {tensor}")

def print_numpy_info(array, name="NumPy Array"):
    """
    Print information about a NumPy array.
    """
    print(f"{name}:")
    print(f"Shape: {array.shape}")
    print(f"Data type: {array.dtype}")
    print(f"Values: {array}")

def print_tf_info(tf_tensor, name="TensorFlow Tensor"):
    """
    Print information about a TensorFlow tensor.
    """
    print(f"{name}:")
    print(f"Shape: {tf_tensor.shape}")
    print(f"Data type: {tf_tensor.dtype}")
    print(f"Values: {tf_tensor}")

# Example usage
if __name__ == "__main__":
    # Create a PyTorch tensor
    torch_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
    print_tensor_info(torch_tensor, "PyTorch Tensor")

    # Convert to NumPy array
    numpy_array = tensor_to_numpy(torch_tensor)
    print_numpy_info(numpy_array, "Converted NumPy Array")

    # Convert to TensorFlow tensor
    tf_tensor = tensor_to_tf(torch_tensor)
    print_tf_info(tf_tensor, "Converted TensorFlow Tensor")