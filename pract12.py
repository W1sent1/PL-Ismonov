import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json
import os
from datetime import datetime

class GitHubRepoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GitHub Repository Info")
        self.root.geometry("600x500")
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(main_frame, text="GitHub Repository Information", 
                               font=('Arial', 14, 'bold'))
        title_label.pack(pady=(0, 20))
        
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="Repository (owner/repo):").pack(side=tk.LEFT)
        self.repo_entry = ttk.Entry(input_frame, width=40)
        self.repo_entry.pack(side=tk.LEFT, padx=10)
        self.repo_entry.insert(0, "kubernetes/kubernetes")
        
        self.get_btn = ttk.Button(input_frame, text="Get Repository Info", 
                                 command=self.get_repo_info)
        self.get_btn.pack(side=tk.LEFT)
        
        ttk.Label(main_frame, text="Result:").pack(anchor=tk.W, pady=(20, 5))
        self.result_text = scrolledtext.ScrolledText(main_frame, height=15, width=70)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        self.save_btn = ttk.Button(main_frame, text="Save to File", 
                                  command=self.save_to_file, state=tk.DISABLED)
        self.save_btn.pack(pady=10)
        
        self.current_data = None
    
    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip()
        if not repo_name:
            messagebox.showerror("Error", "Please enter repository name")
            return
        
        try:
            repo_url = f"https://api.github.com/repos/{repo_name}"
            response = requests.get(repo_url)
            
            if response.status_code == 200:
                repo_data = response.json()
                owner_login = repo_data['owner']['login']
                
                owner_url = f"https://api.github.com/users/{owner_login}"
                owner_response = requests.get(owner_url)
                
                if owner_response.status_code == 200:
                    owner_data = owner_response.json()
                    
                    self.current_data = {
                        'company': owner_data.get('company'),
                        'created_at': owner_data.get('created_at'),
                        'email': owner_data.get('email'),
                        'id': owner_data.get('id'),
                        'name': owner_data.get('name') or owner_data.get('login'),
                        'url': owner_data.get('url')
                    }
                    
                    self.result_text.delete(1.0, tk.END)
                    self.result_text.insert(1.0, json.dumps(self.current_data, indent=2))
                    self.save_btn.config(state=tk.NORMAL)
                    
                else:
                    messagebox.showerror("Error", f"Failed to get owner info: {owner_response.status_code}")
            else:
                messagebox.showerror("Error", f"Repository not found: {response.status_code}")
                
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Network error: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")
    
    def save_to_file(self):
        if not self.current_data:
            return
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"github_repo_info_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.current_data, f, indent=2, ensure_ascii=False)
            
            messagebox.showinfo("Success", f"Data saved to {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def main():
    app = GitHubRepoApp()
    app.root.mainloop()

if __name__ == "__main__":
    main()  