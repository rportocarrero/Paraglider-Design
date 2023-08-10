import numpy as np

edgePoints = np.array([[0,2],[1,2]])
panelPoints = np.array([[0,0],[1,0],[1,1]])

# This function aligns the panel with the edge of the previous panel
def alignPanel(edgePoints, panelPoints):
    edge_vector = edgePoints[1]-edgePoints[0]
    edge_vector = edge_vector/np.linalg.norm(edge_vector)

    panel_vector = panelPoints[1]-panelPoints[0]
    panel_vector = panel_vector/np.linalg.norm(panel_vector)

    # calculate the rotation angle
    rot_angle = np.arctan2(edge_vector[1], edge_vector[0]) - np.arctan2(panel_vector[1], panel_vector[0])

    # calculate the translation vector
    translation_v = edgePoints[0]-panelPoints[0]

    # calculate the rotation
    def build_T_matrix(rot_angle):
        return np.array([[np.cos(rot_angle),-np.sin(rot_angle)],[np.sin(rot_angle),np.cos(rot_angle)]])

    T_matrix = build_T_matrix(rot_angle)

    #Rotate Panel Points
    Rotated_panelPoints = np.dot(T_matrix,panelPoints.T).T

    #Translate Panel Points
    Translated_panelPoints = Rotated_panelPoints + translation_v

    return Translated_panelPoints

new_points = alignPanel(edgePoints, panelPoints)
print(new_points)