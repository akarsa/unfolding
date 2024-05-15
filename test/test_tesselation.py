"""Test tesselation module"""

import numpy as np
from unfolding import unfold_tessellation, create_simplified_tessellation
from unfolding._utils import dummy


def test_create_simplified_tesselation():
    _, label = dummy()
    verts, faces = create_simplified_tessellation(label, num_vertices=30)
    verts_true = np.load("test/verts.npy")
    faces_true = np.load("test/faces.npy")
    assert np.linalg.norm(verts - verts_true) < 1e-3
    assert np.linalg.norm(faces - faces_true) < 1e-3


def test_unfold_tessellation():
    verts_true = np.load("test/verts.npy")
    faces_true = np.load("test/faces.npy")
    verts_2d_true = np.load("test/verts_2d.npy")
    faces_2d_true = np.load("test/faces_2d.npy")
    verts_2d, faces_2d, dict_2d_3d = unfold_tessellation(verts_true, faces_true)
    np.save("dict_2d_3d.npy", dict_2d_3d)
    assert np.linalg.norm(verts_2d - verts_2d_true) < 1e-3
    assert np.linalg.norm(faces_2d - faces_2d_true) < 1e-3
