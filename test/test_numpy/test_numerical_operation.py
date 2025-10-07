import pytest

# Test data
MATRIX_2X2 = [[1, 2], [3, 4]]

# Test data
MATRIX_2X2 = [[1, 2], [3, 4]]
MATRIX_3X3 = [[4, 1, 2], [1, 5, 3], [2, 3, 6]]
VECTOR_1D = [1, 2, 3, 4, 5]
VECTOR_2D = [[1, 2, 3], [4, 5, 6]]


@pytest.mark.asyncio
async def test_numerical_operations(client):
    """Test various numerical operations using the FastAPI test client."""
    # Test create_array
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "create_array", "a": [1, 2, 3]},
    )
    assert response.data == [1, 2, 3]

    # Test zeros
    response = await client.call_tool(
        "numpy_mcp_numerical_operation", {"operation": "zeros", "shape": [2, 3]}
    )
    assert response.data == [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

    # Test ones
    response = await client.call_tool(
        "numpy_mcp_numerical_operation", {"operation": "ones", "shape": [2, 2]}
    )
    assert response.data == [[1.0, 1.0], [1.0, 1.0]]

    # Test full
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "full", "shape": [2, 2], "fill_value": 5},
    )
    assert response.data == [[5.0, 5.0], [5.0, 5.0]]

    # Test reshape
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "reshape", "a": [1, 2, 3, 4], "new_shape": [2, 2]},
    )
    assert response.data == [[1, 2], [3, 4]]

    # Test flatten
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "flatten", "a": [[1, 2], [3, 4]]},
    )
    assert response.data == [1, 2, 3, 4]

    # Test transpose
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "transpose", "a": [[1, 2], [3, 4]]},
    )
    assert response.data == [[1, 3], [2, 4]]

    # Test add
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "add", "a": [1, 2, 3], "b": [4, 5, 6]},
    )
    assert response.data == [5, 7, 9]

    # Test multiply
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "multiply", "a": [1, 2, 3], "b": [4, 5, 6]},
    )
    assert response.data == [4, 10, 18]

    # Test power
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "power", "a": [2, 3, 4], "b": [2, 3, 0.5]},
    )
    assert response.data == [4.0, 27.0, 2.0]

    # Test mean
    response = await client.call_tool(
        "numpy_mcp_numerical_operation", {"operation": "mean", "a": [1, 2, 3, 4, 5]}
    )
    assert response.data == 3.0

    # Test std
    response = await client.call_tool(
        "numpy_mcp_numerical_operation", {"operation": "std", "a": [1, 2, 3, 4, 5]}
    )
    assert abs(response.data - 1.4142) < 0.0001

    # Test dot product
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "dot", "a": [1, 2, 3], "b": [4, 5, 6]},
    )
    assert response.data == 32.0

    # Test matrix multiplication
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "matmul", "a": [[1, 2], [3, 4]], "b": [[5, 6], [7, 8]]},
    )
    assert response.data == [[19.0, 22.0], [43.0, 50.0]]

    # Test determinant
    response = await client.call_tool(
        "numpy_mcp_numerical_operation", {"operation": "det", "a": [[4, 7], [2, 6]]}
    )
    assert response.data == pytest.approx(10.0)

    # Test matrix inverse
    response = await client.call_tool(
        "numpy_mcp_numerical_operation", {"operation": "inv", "a": [[4, 7], [2, 6]]}
    )
    expected = [[0.6, -0.7], [-0.2, 0.4]]
    for r, e in zip(response.data, expected):
        for a, b in zip(r, e):
            assert abs(a - b) < 1e-10

    # Test eigenvalues and eigenvectors
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "eig", "a": [[1, -1], [1, 1]]},
    )
    assert len(response.data["eigenvalues"]) == 2
    assert len(response.data["eigenvectors"]) == 2
    assert len(response.data["eigenvectors"][0]) == 2

    # Test eigenvalues only
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "eigenvals", "a": [[4, 1], [2, 3]]},
    )
    assert len(response.data) == 2
    assert all(isinstance(x, (float, complex)) for x in response.data)

    # Test solving linear system
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "solve", "a": [[3, 1], [1, 2]], "b": [9, 8]},
    )
    expected = [2.0, 3.0]
    for r, e in zip(response.data, expected):
        assert abs(r - e) < 1e-10

    # Test SVD
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "svd", "a": [[1, 2], [3, 4], [5, 6]]},
    )
    assert len(response.data["U"]) == 3
    assert len(response.data["S"]) == 2
    assert len(response.data["Vt"]) == 2

    # Test invalid operation
    with pytest.raises(Exception) as exc_info:
        await client.call_tool(
            "numpy_mcp_numerical_operation",
            {"operation": "invalid_operation", "a": [1, 2, 3]},
        )
    assert "Unknown operation" in str(exc_info.value)

    # Test empty array - expect an error
    with pytest.raises(Exception) as exc_info:
        await client.call_tool(
            "numpy_mcp_numerical_operation", {"operation": "mean", "a": []}
        )
    assert "Invalid structured content" in str(exc_info.value)

    # Test matrix multiplication dimension mismatch
    with pytest.raises(Exception) as exc_info:
        await client.call_tool(
            "numpy_mcp_numerical_operation",
            {"operation": "matmul", "a": [[1, 2], [3, 4]], "b": [1, 2, 3]},
        )
    assert "mismatch in its core dimension" in str(exc_info.value)

    # Test real number operations
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "add", "a": [1, 2, 3], "b": [4, 5, 6]},
    )
    assert response.data == [5, 7, 9]

    # Test matrix multiplication with real numbers
    response = await client.call_tool(
        "numpy_mcp_numerical_operation",
        {"operation": "matmul", "a": [[1, 2], [3, 4]], "b": [[5, 6], [7, 8]]},
    )
    assert response.data == [[19.0, 22.0], [43.0, 50.0]]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
    # Test matrix multiplication with real numbers
