"my-comp": {
	alias: ""
	annotations: {}
	attributes: workload: definition: {
		apiVersion: "apps/v1"
		kind:       "Deployment"
	}
	description: "My component."
	labels: {}
	type: "component"
}

template: {
	output: {
		apiVersion: "apps/v1"
		kind:       "Deployment"
		metadata: name: "hello-world"
		spec: {
			replicas: 1
			selector: matchLabels: "app.kubernetes.io/name": "hello-world"
			template: {
				metadata: labels: "app.kubernetes.io/name": "hello-world"
				spec: containers: [{
					image: "somefive/hello-world"
					name:  "hello-world"
					ports: [{
						containerPort: 80
						name:          "http"
						protocol:      "TCP"
					}]
				}]
			}
		}
	}
	outputs: "hello-world-service": {
		apiVersion: "v1"
		kind:       "Service"
		metadata: name: "hello-world-service"
		spec: {
			ports: [{
				name:       "http"
				port:       80
				protocol:   "TCP"
				targetPort: 8080
			}]
			selector: app: "hello-world"
			type: "LoadBalancer"
		}
	}
	parameter: {}
}

