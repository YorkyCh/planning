import axios from "axios";

export const getProjects = async () => {
  try {
    const response = await axios.get("/api/projects");
    return response.data;
  } catch (error) {
    console.error("Error fetching projects:", error);
    throw error;
  }
};

// You can add more API-related functions here
