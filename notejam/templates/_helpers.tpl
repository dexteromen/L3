{{/*
Common labels
*/}}
{{- define "notejam.labels" -}}
app.kubernetes.io/name: {{ include "notejam.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Chart name
*/}}
{{- define "notejam.name" -}}
{{ .Chart.Name }}
{{- end }}
