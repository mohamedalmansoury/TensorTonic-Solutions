def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.array(v, dtype=float)

    if v.ndim == 1:
        norm = np.linalg.norm(v)
        return v / norm if norm > 1e-10 else v

    norms = np.linalg.norm(v, axis=1, keepdims=True)

    result = np.zeros_like(v)
    mask = (norms > 1e-10).flatten()
    result[mask] = v[mask] / norms[mask]
    return result
