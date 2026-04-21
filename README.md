# VertexColourDeformation
A system for pre planned deformation of meshes through Python &amp; shading.

<h1>Maya</h1>
<p align="center" width="100%">
<video src="https://github.com/user-attachments/assets/563d36e5-1c92-49e6-aa88-c873a20ddf1d](https://github.com/user-attachments/assets/fc1cbc1a-aa5d-4f6c-89f2-4ca5240a9de4" width="80%" controls></video>
</p>

This video shows how to use the python script in Maya. Create a copy of your original mesh, then apply the deformation to the vertices that you want. Once done, select the source mesh, then the destination mesh. Run the script, and the positions are now stored as vertex colours on the original mesh. This data can then be used in a game engine to deform the mesh in a cheap way.

<h1>In Engine - Unity</h1>
<p align="center" width="100%">
<video src="https://github.com/user-attachments/assets/16ad3f79-2737-4293-bc94-05392da81d13" width="80%" controls></video>
</p>

The data can be accessed in the vertex shader and deform the mesh in the predefined way. This can be a useful and cheap way to deform a mesh without needing to rely on processing the mesh at run time which can cause stuttering or loss of hard/soft edges (looking at you, Unity).

<h1>Shading - Unity</h1>
<img width="2286" height="1358" alt="image" src="https://github.com/user-attachments/assets/656e2a3f-a8ac-4132-920b-3891a88f1953" />

To use the new vertex colours in your shader, download the Unity shader sub graph and add it to your shader, with a float input, and connect the output to Position in the Vertex Group.
